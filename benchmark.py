# Benchmark outline: generate 1, 12 and 120 stations x 8,760 hourly rows.
# Run each method several times and report the median elapsed time.
import time
import statistics


def measure(fn, repeats=3):
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        fn()
        times.append(time.perf_counter() - start)
    return statistics.median(times)


# For each station count in (1, 12, 120):
# 1) generate a CSV file with station,date,pm25 rows
# 2) time the loop, pandas groupby and SQL GROUP BY separately
# 3) verify each result agrees before recording its time
# 4) report rows = station_count * 8760
