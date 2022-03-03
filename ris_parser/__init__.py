from .io import reader, writer, DictReader, DictWriter  # noqa


def read_ris(filepath, encoding='utf-8-sig'):
    """A convenience generator that wraps ris.DictReader and yields entries"""
    with open(filepath, 'r', encoding=encoding) as f:
        fr = DictReader(f)
        for entry in fr:
            yield entry


def write_ris(filepath, data, encoding='utf-8'):
    """A convenience function that wraps ris.DictWriter"""
    with open(filepath, 'w', encoding=encoding) as f:
        fw = DictWriter(f)
        try:
            fw.write_entries(data)
        except TypeError:
            fw.write_entry(data)
