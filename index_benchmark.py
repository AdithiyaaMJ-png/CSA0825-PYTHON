import sqlite3
import time

con = sqlite3.connect("air_quality.db")
query = "SELECT AVG(pm25) FROM readings WHERE station_id=? AND reading_date=?"
params = (1, "2026-10-01")


def elapsed():
    start = time.perf_counter()
    for _ in range(500):
        con.execute(query, params).fetchone()
    return time.perf_counter() - start


before = elapsed()
con.execute("CREATE INDEX IF NOT EXISTS idx_station_day ON readings(station_id, reading_date)")
con.commit()
after = elapsed()

print("Before index:", before)
print("After index:", after)
con.close()
