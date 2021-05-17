import re

cnic_end_patterns = [
    "affliation",
    "Physical Structure",
    "Passport No.",
    "religious",
    "reference order"
    "S.No.",
    "Religious",
    "Any other",
    'Other information',
    'His Notification',
    "Crime History",
    "address",
    "2 million"
]

name_end_patterns = [
    "Address"
]


def get_cnic_end_index(text):
    for pattern in cnic_end_patterns:
        pattern = pattern.lower()
        if pattern in text:
            return text.index(pattern)
    return 0


def get_cnic_text(text):
    text = text.lower()
    if text.find("cnic no.") != -1:
        start_idx = text.index("cnic") + 12
    else:
        start_idx = text.index("cnic") + 4
    end_idx_cnic = get_cnic_end_index(text[start_idx:])
    if end_idx_cnic != 0:
        end_idx = start_idx + end_idx_cnic
        text_cnic = text[start_idx:end_idx]
    else:
        text_cnic = text[start_idx:]
    return text_cnic


def get_name_end_index(text):
    for nam_pat in name_end_patterns:
        nam_pat = nam_pat.lower()
        if nam_pat in text:
            return text.index(nam_pat)
    return 0


def get_name_text(text):
    text = text.lower()
    if text.find("name & parentage") != -1:
        start_id = text.index("name") + 16
    else:
        start_id = text.index("name") + 4
    end_id = start_id + get_name_end_index(text[start_id:])
    text_name = text[start_id:end_id]

    return text_name


def get_name_att(name):
    if name.find('s/o') != -1:
        name_ = re.split('s/o', name)
    else:
        name_ = re.split('f/name:', name)
    return name_
