def subsidy_separate(units, ration_card, senior_member):
    result = []

    if units <= 100:
        result.append("Full subsidy")

    if 101 <= units <= 200 and ration_card:
        result.append("Partial subsidy")

    if units > 200 and senior_member:
        result.append("Special subsidy")

    if not result:
        result.append("No subsidy")

    return result


def subsidy(units, ration_card, senior_member):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        if ration_card:
            return "Partial subsidy"
        return "No subsidy"
    elif units > 200:
        if senior_member:
            return "Special subsidy"
        return "No subsidy"


def subsidy_lookup(units, ration_card, senior_member):
    if units <= 100:
        return "Full subsidy"
    if units <= 200:
        return "Partial subsidy" if ration_card else "No subsidy"
    return "Special subsidy" if senior_member else "No subsidy"
