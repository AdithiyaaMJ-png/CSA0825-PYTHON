def normalise(text):
    return text.strip().replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    if len(reg) not in (9, 10):
        return False

    return (
        reg[0:2].isalpha()
        and reg[2:4].isdigit()
        and reg[4:-4].isalpha()
        and len(reg[4:-4]) in (1, 2)
        and reg[-4:].isdigit()
    )


def format_number(reg):
    if not is_valid(reg):
        return "Invalid registration number"

    return f"{reg[0:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"


samples = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "mh 12 xy 9876",
    "XX-99-ZZ-123"
]

for raw in samples:
    reg = normalise(raw)
    print(raw, "->", reg, "->",
          format_number(reg) if is_valid(reg) else "INVALID")


import re

def is_valid_regex(reg):
    return re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg) is not None
