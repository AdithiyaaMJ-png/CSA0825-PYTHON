def normalise_number(number):
    digits = "".join(ch for ch in number if ch.isdigit())
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits

def normalise_name(name):
    return " ".join(name.lower().strip().split())

def merge_contacts(contact_lists):
    merged = {}
    for contacts in contact_lists:
        for contact in contacts:
            numbers = {
                normalise_number(number)
                for number in contact.get("numbers", [])
            }
            numbers.discard("")
            if not numbers:
                # Contacts without a usable number are kept separately.
                key = "NO_NUMBER_" + str(len(merged) + 1)
            else:
                key = sorted(numbers)[0]

            if key not in merged:
                merged[key] = {
                    "names": set(),
                    "numbers": set(),
                    "emails": set()
                }

            name = contact.get("name", "").strip()
            if name:
                merged[key]["names"].add(name)
            merged[key]["numbers"].update(numbers)
            merged[key]["emails"].update(
                email.lower().strip()
                for email in contact.get("emails", []) if email.strip()
            )
    return merged

phone_a = [
    {"name": "Dr. Ravi", "numbers": ["+91 98400 12345"],
     "emails": ["ravi@example.com"]},
    {"name": "Meena", "numbers": ["9876543210"],
     "emails": ["meena@example.com"]}
]
phone_b = [
    {"name": "ravi kumar", "numbers": ["9840012345", "044 22223333"],
     "emails": ["RAVI@example.com", "rk@example.com"]},
    {"name": "Arun", "numbers": [], "emails": ["arun@example.com"]}
]

result = merge_contacts([phone_a, phone_b])
for key, details in sorted(result.items()):
    print("Key:", key)
    print("Names:", sorted(details["names"]))
    print("Numbers:", sorted(details["numbers"]))
    print("Emails:", sorted(details["emails"]))
    print()
