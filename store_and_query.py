import sqlite3

clean = [
    ("Adyar", "2026-10-01", 48.0),
    ("Guindy", "2026-10-01", 95.0),
    ("Guindy", "2026-10-03", 121.0)
]

con = sqlite3.connect("air_quality.db")
con.execute("""
CREATE TABLE IF NOT EXISTS aq (
    station TEXT,
    day TEXT,
    pm25 REAL,
    PRIMARY KEY(station, day)
)
""")
con.executemany(
    "INSERT OR REPLACE INTO aq(station, day, pm25) VALUES (?, ?, ?)",
    clean
)
con.commit()

# 1. Average PM2.5 for Adyar in October 2026
q1 = con.execute(
    "SELECT AVG(pm25) FROM aq WHERE station=? AND day BETWEEN ? AND ?",
    ("Adyar", "2026-10-01", "2026-10-31")
).fetchone()[0]

# 2. Station with highest average
q2 = con.execute(
    "SELECT station, AVG(pm25) AS avg_pm FROM aq GROUP BY station ORDER BY avg_pm DESC LIMIT 1"
).fetchone()

# 3. Readings above 100
q3 = con.execute(
    "SELECT station, day, pm25 FROM aq WHERE pm25 > ? ORDER BY day",
    (100,)
).fetchall()

print(q1, q2, q3)
con.close()
