
# Cf. https://en.wikipedia.org/wiki/RIS_(file_format), Aug-13-2019
REFERENCE_TYPES = {
    'ABST': 'Abstract',
    'ADVS': 'Audiovisual material',
    'AGGR': 'Aggregated Database',
    'ANCIENT': 'Ancient Text',
    'ART': 'Art Work',
    'BILL': 'Bill',
    'BLOG': 'Blog',
    'BOOK': 'Whole book',
    'CASE': 'Case',
    'CHAP': 'Book chapter',
    'CHART': 'Chart',
    'CLSWK': 'Classical Work',
    'COMP': 'Computer program',
    'CONF': 'Conference proceeding',
    'CPAPER': 'Conference paper',
    'CTLG': 'Catalog',
    'DATA': 'Data file',
    'DBASE': 'Online Database',
    'DICT': 'Dictionary',
    'EBOOK': 'Electronic Book',
    'ECHAP': 'Electronic Book Section',
    'EDBOOK': 'Edited Book',
    'EJOUR': 'Electronic Article',
    'ELEC': 'Web Page',
    'ENCYC': 'Encyclopedia',
    'EQUA': 'Equation',
    'FIGURE': 'Figure',
    'GEN': 'Generic',
    'GOVDOC': 'Government Document',
    'GRANT': 'Grant',
    'HEAR': 'Hearing',
    'ICOMM': 'Internet Communication',
    'INPR': 'In Press',
    'JFULL': 'Journal (full)',
    'JOUR': 'Journal',
    'LEGAL': 'Legal Rule or Regulation',
    'MANSCPT': 'Manuscript',
    'MAP': 'Map',
    'MGZN': 'Magazine article',
    'MPCT': 'Motion picture',
    'MULTI': 'Online Multimedia',
    'MUSIC': 'Music score',
    'NEWS': 'Newspaper',
    'PAMP': 'Pamphlet',
    'PAT': 'Patent',
    'PCOMM': 'Personal communication',
    'RPRT': 'Report',
    'SER': 'Serial publication',
    'SLIDE': 'Slide',
    'SOUND': 'Sound recording',
    'STAND': 'Standard',
    'STAT': 'Statute',
    'THES': 'Thesis/Dissertation',
    'UNPB': 'Unpublished work',
    'VIDEO': 'Video recording',
}

# Cf. https://en.wikipedia.org/wiki/RIS_(file_format), Aug-13-2019
STANDARD_TAGS = {
    'TY': {
        'description': 'Type of reference',
        'notes': 'must be the first tag'
    },
    'A1': {
        'description': 'First Author'
    },
    'A2': {
        'description': 'Secondary Author',
        'notes': 'each author on its own line preceded by the tag'
    },
    'A3': {
        'description': 'Tertiary Author',
        'notes': 'each author on its own line preceded by the tag'
    },
    'A4': {
        'description': 'Subsidiary Author',
        'notes': 'each author on its own line preceded by the tag'
    },
    'AB': {
        'description': 'Abstract'
    },
    'AD': {
        'description': 'Author Address'
    },
    'AN': {
        'description': 'Accession Number'
    },
    'AU': {
        'description': 'Author',
        'notes': 'each author on its own line preceded by the tag'
    },
    'AV': {
        'description': 'Location in Archives'
    },
    'BT': {
        'description': (
            'This field maps to T2 for all reference types '
            'except for Whole Book and Unpublished Work references.'
        ),
        'notes': (
            'It can contain alphanumeric characters. '
            'There is no practical limit to the length of this field.'
        )
    },
    'C1': {
        'description': 'Custom 1'
    },
    'C2': {
        'description': 'Custom 2'
    },
    'C3': {
        'description': 'Custom 3'
    },
    'C4': {
        'description': 'Custom 4'
    },
    'C5': {
        'description': 'Custom 5'
    },
    'C6': {
        'description': 'Custom 6'
    },
    'C7': {
        'description': 'Custom 7'
    },
    'C8': {
        'description': 'Custom 8'
    },
    'CA': {
        'description': 'Caption'
    },
    'CN': {
        'description': 'Call Number'
    },
    'CP': {
        'notes': (
            'This field can contain alphanumeric characters. '
            'There is no practical limit to the length of this field.'
        )
    },
    'CT': {
        'description': 'Title of unpublished reference'
    },
    'CY': {
        'description': 'Place Published'
    },
    'DA': {
        'description': 'Date'
    },
    'DB': {
        'description': 'Name of Database'
    },
    'DO': {
        'description': 'DOI'
    },
    'DP': {
        'description': 'Database Provider'
    },
    'ED': {
        'description': 'Editor'
    },
    'EP': {
        'description': 'End Page'
    },
    'ET': {
        'description': 'Edition'
    },
    'ID': {
        'description': 'Reference ID'
    },
    'IS': {
        'description': 'Issue number'
    },
    'J1': {
        'description': 'Periodical name: user abbreviation 1. ',
        'notes': 'This is an alphanumeric field of up to 255 characters.'
    },
    'J2': {
        'description': 'Alternate Title',
        'notes': (
            'this field is used for the abbreviated title '
            'of a book or journal name, the latter mapped to T2'
        )
    },
    'JA': {
        'description': 'Periodical name: standard abbreviation.',
        'notes': (
            'This is the periodical in which the article was '
            '(or is to be, in the case of in-press references) '
            'published. '
            'This is an alphanumeric field of up to 255 characters.'
        )
    },
    'JF': {
        'description': 'Journal/Periodical name: full format.',
        'notes': (
            'This is an alphanumeric field of up to 255 characters.'
        )
    },
    'JO': {
        'description': 'Journal/Periodical name: full format.',
        'notes': 'This is an alphanumeric field of up to 255 characters.'
    },
    'KW': {
        'description': 'Keywords',
        'notes': (
            'keywords should be entered each on its own line '
            'preceded by the tag'
        )
    },
    'L1': {
        'description': 'Link to PDF.',
        'notes': (
            'There is no practical limit to the length of this field. '
            'URL addresses can be entered individually, '
            'one per tag or multiple addresses can be entered '
            'on one line using a semi-colon as a separator.'
        )
    },
    'L2': {
        'description': 'Link to Full-text.',
        'notes': (
            'There is no practical limit to the length of this field.'
            'URL addresses can be entered individually, '
            'one per tag or multiple addresses can be entered '
            'on one line using a semi-colon as a separator.'
        )
    },
    'L3': {
        'description': 'Related Records.',
        'notes': (
            'There is no practical limit to the length of this field.'
        )
    },
    'L4': {
        'description': 'Image(s).',
        'notes': (
            'There is no practical limit to the length of this field.'
        )
    },
    'LA': {
        'description': 'Language'
    },
    'LB': {
        'description': 'Label'
    },
    'LK': {
        'description': 'Website Link'
    },
    'M1': {
        'description': 'Number'
    },
    'M2': {
        'description': 'Miscellaneous 2.',
        'notes': (
            'This is an alphanumeric field '
            'and there is no practical limit to the length of this field.'
        )
    },
    'M3': {
        'description': 'Type of Work'
    },
    'N1': {
        'description': 'Notes'
    },
    'N2': {
        'description': 'Abstract.',
        'notes': (
            'This is a free text field '
            'and can contain alphanumeric characters. '
            'There is no practical length limit to this field.'
        )
    },
    'NV': {
        'description': 'Number of Volumes'
    },
    'OP': {
        'description': 'Original Publication'
    },
    'PB': {
        'description': 'Publisher'
    },
    'PP': {
        'description': 'Publishing Place'
    },
    'PY': {
        'description': 'Publication year (YYYY)'
    },
    'RI': {
        'description': 'Reviewed Item'
    },
    'RN': {
        'description': 'Research Notes'
    },
    'RP': {
        'description': 'Reprint Edition'
    },
    'SE': {
        'description': 'Section'
    },
    'SN': {
        'description': 'ISBN/ISSN'
    },
    'SP': {
        'description': 'Start Page'
    },
    'ST': {
        'description': 'Short Title'
    },
    'T1': {
        'description': 'Primary Title'
    },
    'T2': {
        'description': 'Secondary Title (journal title, if applicable)'
    },
    'T3': {
        'description': 'Tertiary Title'
    },
    'TA': {
        'description': 'Translated Author'
    },
    'TI': {
        'description': 'Title'
    },
    'TT': {
        'description': 'Translated Title'
    },
    'U1': {
        'description': 'User definable 1.',
        'notes': (
            'This is an alphanumeric field '
            'and there is no practical limit to the length of this field.'
        )
    },
    'U2': {
        'description': 'User definable 2.',
        'notes': (
            'This is an alphanumeric field '
            'and there is no practical limit to the length of this field.'
        )
    },
    'U3': {
        'description': 'User definable 3.',
        'notes': (
            'This is an alphanumeric field '
            'and there is no practical limit to the length of this field.'
        )
    },
    'U4': {
        'description': 'User definable 4.',
        'notes': (
            'This is an alphanumeric field '
            'and there is no practical limit to the length of this field.'
        )
    },
    'U5': {
        'description': 'User definable 5.',
        'notes': (
            'This is an alphanumeric field '
            'and there is no practical limit to the length of this field.'
        )
    },
    'UR': {
        'description': 'URL'
    },
    'VL': {
        'description': 'Volume number'
    },
    'VO': {
        'description': 'Published Standard number'
    },
    'Y1': {
        'description': 'Primary Date'
    },
    'Y2': {
        'description': 'Access Date'
    },
    'ER': {
        'description': 'End of Reference',
        'notes': 'must be empty and the last tag'
    }
}
