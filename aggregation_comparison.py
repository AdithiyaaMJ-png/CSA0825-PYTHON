import csv
import io
import sqlite3
from collections import defaultdict
import pandas as pd

sample = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-01,52
Adyar,2026-10-02,40
Guindy,2026-10-01,90
Guindy,2026-10-01,100"""

# Method 1: csv module + Python loops
acc = defaultdict(lambda: [0.0, 0])
for row in csv.DictReader(io.StringIO(sample)):
    key = (row["station"], row["date"])
    acc[key][0] += float(row["pm25"])
    acc[key][1] += 1
loop_result = {k: total / count for k, (total, count) in acc.items()}

# Method 2: pandas groupby
df = pd.read_csv(io.StringIO(sample))
pandas_result = df.groupby(["station", "date"])["pm25"].mean().to_dict()

# Method 3: SQLite GROUP BY
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE readings(station TEXT, day TEXT, pm25 REAL)")
con.executemany(
    "INSERT INTO readings VALUES (?, ?, ?)",
    [(r["station"], r["date"], float(r["pm25"]))
     for r in csv.DictReader(io.StringIO(sample))]
)
sql_result = {
    (s, d): m for s, d, m in con.execute(
        "SELECT station, day, AVG(pm25) FROM readings GROUP BY station, day"
    )
}
con.close()

print(loop_result)
print(pandas_result)
print(sql_result)
assert loop_result == pandas_result == sql_result
