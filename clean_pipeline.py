import csv
import io

RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
Guindy,2026-10-04,1200"""


def load_clean(text):
    """Return valid (station, date, pm25) tuples."""
    rows = []
    reader = csv.DictReader(io.StringIO(text))
    required = {"station", "date", "pm25"}
    if not reader.fieldnames or not required.issubset(reader.fieldnames):
        raise ValueError("CSV is missing a required column")
    for row in reader:
        raw = (row.get("pm25") or "").strip()
        if raw == "" or raw.upper() == "NA":
            continue
        try:
            value = float(raw)
        except ValueError:
            continue
        if value < 0 or value > 999:
            continue
        rows.append((row["station"].strip(), row["date"].strip(), value))
    return rows


def min_max(values):
    if not values:
        return []
    low, high = min(values), max(values)
    if high == low:
        return [0.0 for _ in values]
    return [round((v - low) / (high - low), 3) for v in values]


if __name__ == "__main__":
    clean = load_clean(RAW)
    print(clean)
    print(min_max([pm for _, _, pm in clean]))
