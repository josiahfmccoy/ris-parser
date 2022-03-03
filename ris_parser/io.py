from collections import defaultdict
from .standards import REFERENCE_TYPES, STANDARD_TAGS

__all__ = ['reader', 'writer', 'DictReader', 'DictWriter']


class RisIoBase:
    """Base class for any class that handles RIS I/O"""
    start_tag = 'TY'
    ref_tag = 'TY'
    id_tag = 'ID'
    end_tag = 'ER'

    asterisk_restricted = [
        'AU', 'A1', 'A2', 'A3', 'ED', 'KW',
        'JF', 'JO', 'JA', 'J1', 'J2'
    ]

    _tag_delimiter = '  - '

    def _validate_tag(self, tag):
        if tag in STANDARD_TAGS:
            return  # Standard tags are valid by definition
        if not isinstance(tag, str):
            raise IOError(f"Invalid RIS Tag: '{tag}'")
        if not (len(tag) == 2 and tag[0].isalpha() and tag[1].isalnum()):
            raise IOError(f"Invalid RIS Tag: '{tag}'")

    def _validate_ref_type(self, ref_type):
        if ref_type not in REFERENCE_TYPES:
            raise IOError(f"Invalid RIS Reference Type: '{ref_type}'")

    def _validate_ref_id(self, ref_id):
        if not ref_id.isalnum() or len(ref_id) > 20:
            raise IOError(
                f"Invalid RIS Reference ID: '{ref_id}'"
            )

    def _validate_asterisks(self, tag, value):
        if not self.check_asterisks:
            return
        asteriskError = IOError(
            f"Invalid value for '{tag}'. "
            f"The {tag} tag is not allowed to contain "
            "asterisks according to the RIS standards, "
            f"but at least one asterisk was found in: '{value}'"
        )
        if tag in self.asterisk_restricted:
            if isinstance(value, list):
                for text in value:
                    if '*' in text:
                        raise asteriskError
            elif '*' in value:
                raise asteriskError

    def _validate_entry(self, entry):
        if self.start_tag not in entry:
            raise IOError(
                f"Mandatory '{self.start_tag}' tag "
                f"not present in '{entry}'"
            )
        for tag, value in entry.items():
            # Is the tag properly formatted?
            self._validate_tag(tag)
            # Is the reference type in the allowed field names?
            if tag == self.ref_tag:
                self._validate_ref_type(value)
            # Is the reference id properly formatted?
            if tag == self.id_tag:
                self._validate_ref_id(value)
            # Does the reference lack asterisks if restricted?
            self._validate_asterisks(tag, value)

    def __init__(
        self, *args,
        start_tag='TY', ref_tag='TY', id_tag='ID', end_tag='ER',
        check_asterisks=False,
        **kwargs
    ):
        if isinstance(start_tag, str) and self._validate_tag(start_tag):
            self.start_tag = start_tag

        if isinstance(ref_tag, str) and self._validate_tag(ref_tag):
            self.ref_tag = ref_tag

        if isinstance(id_tag, str) and self._validate_tag(id_tag):
            self.id_tag = id_tag

        if isinstance(end_tag, str) and self._validate_tag(end_tag):
            self.end_tag = end_tag

        self.check_asterisks = check_asterisks


class DictReader(RisIoBase):
    """A reader object (based on csv.DictReader) for parsing RIS files."""

    def __init__(
        self, risfile, *args, strict_tags=False, **kwargs
    ):
        self.risfile = risfile
        self._lines = iter(risfile.readlines())
        self.strict_tags = strict_tags
        super().__init__(*args, **kwargs)

    def __iter__(self):
        return self

    @property
    def FormatError(self):
        if hasattr(self.risfile, 'filename'):
            ris_name = self.risfile.filename
        else:
            ris_name = self.risfile
        return IOError(
            f"'{ris_name}' is not a properly formatted RIS file."
        )

    def __next__(self):
        entry = defaultdict(str)
        end_string = self.end_tag + self._tag_delimiter
        tag = None

        # Get the delimiter we will use to split tags
        delim = self._tag_delimiter
        if not self.strict_tags:
            # non-strict mode ignores final space(s) in tags
            # (or lack thereof)
            delim = delim.rstrip()

        for i, next_row in enumerate(self._lines):
            if isinstance(next_row, bytes):
                next_row = next_row.decode('utf-8-sig')
            if next_row.startswith(end_string):
                break
            if next_row.strip() == '':
                continue

            row = next_row.split(delim, 1)

            if len(row) == 2:
                tag = row[0].strip()
                text = row[1].strip()
            elif len(row) == 1:
                text = row[0].strip()
            else:
                raise self.FormatError

            if tag is None and text is not None:
                err = IOError(
                    'There is no valid RIS tag associated with'
                    f' line {i + 1}: {text}'
                )
                raise self.FormatError from err

            if tag in entry:
                if len(row) == 2:
                    # This is a repeat tag, so make it a list
                    if not isinstance(entry[tag], list):
                        entry[tag] = [entry[tag]]
                    entry[tag].append(text)
                else:
                    # This is a tagless row; concat with last entry
                    if isinstance(entry[tag], list):
                        # Last entry was list, so this goes onto
                        # the last item of the list
                        last = entry[tag][-1]
                        last = '\n'.join([last, text]).strip()
                        entry[tag][-1] = last
                    else:
                        # Last entry was a string, so this goes onto
                        # the string directly
                        entry[tag] = '\n'.join([entry[tag], text])
            else:
                # This is a new tag row
                entry[tag] = text

        if len(entry.keys()) == 0:
            # Empty entry must mean end of file
            raise StopIteration

        try:
            self._validate_entry(entry)
        except Exception as e:
            raise self.FormatError from e
        return dict(entry)


class DictWriter(RisIoBase):
    """A writer object (based on csv.DictWriter) for parsing RIS files."""

    def __init__(self, risfile, *args, **kwargs):
        self.risfile = risfile
        super().__init__(*args, **kwargs)

    def _writeline(self, line):
        self.risfile.writelines([f'{line}\n'])

    def write_entry(self, entry):
        entrydict = dict(entry)

        self._validate_entry(entrydict)

        # Force the start tag to be first, if present
        start = entrydict.pop(self.start_tag, None)
        if start is not None:
            self._writeline(
                f'{self.start_tag}{self._tag_delimiter}{start}'
            )

        # Then write the other tags
        for tag, value in entrydict.items():
            if not value:
                continue  # Skip empty tags (no need to write those)
            if isinstance(value, list):
                # Convert to multiple tags
                for text in value:
                    self._writeline(f'{tag}{self._tag_delimiter}{text}')
            else:
                # Just a single tag
                self._writeline(f'{tag}{self._tag_delimiter}{value}')

        # Finally, write the end tag
        self._writeline(f'{self.end_tag}{self._tag_delimiter}')
        # And close with two more newlines
        self._writeline('\n')

    def write_entries(self, entries):
        for entry in entries:
            self.write_entry(entry)


class reader(DictReader):
    """
    A wrapper for ris.io.DictReader.
    Unlike in the csv module, there is no difference between these classes.
    """


class writer(DictWriter):
    """
    A wrapper for ris.io.DictWriter.
    Unlike in the csv module, there is no difference between these classes.
    """
