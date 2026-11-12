import random
import time

random.seed(10)
readings = [round(random.uniform(0, 30), 1) for _ in range(365)]

weekly_totals = [
    round(sum(readings[i:i + 7]), 1)
    for i in range(0, len(readings), 7)
]
wettest_week = max(range(len(weekly_totals)), key=weekly_totals.__getitem__)
driest_week = min(range(len(weekly_totals)), key=weekly_totals.__getitem__)

naive_average = [
    sum(readings[i:i + 7]) / 7
    for i in range(len(readings) - 6)
]

running_average = []
if len(readings) >= 7:
    window_sum = sum(readings[:7])
    running_average.append(window_sum / 7)
    for i in range(7, len(readings)):
        window_sum += readings[i] - readings[i - 7]
        running_average.append(window_sum / 7)

dry_days = [i + 1 for i, value in enumerate(readings) if value == 0]

print("Number of readings:", len(readings))
print("Number of weekly totals:", len(weekly_totals))
print("Wettest week:", wettest_week + 1, "Total:", weekly_totals[wettest_week])
print("Driest week:", driest_week + 1, "Total:", weekly_totals[driest_week])
print("Moving averages match:", all(
    abs(a - b) < 1e-9 for a, b in zip(naive_average, running_average)
))
print("Dry days:", dry_days)
print("readings[7:14]:", readings[7:14])
print("readings[-7:]:", readings[-7:])
print("readings[::7] first five:", readings[::7][:5])

# Empty and shorter-than-seven inputs
for sample in ([], [2, 4, 6]):
    print("Short input", sample, "->", [
        sum(sample[i:i + 7]) / 7 for i in range(max(0, len(sample) - 6))
    ])
