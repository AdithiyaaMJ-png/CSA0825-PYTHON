import time
import sys

readings = [4.0, 5.5, 55.0, -60.0, 9.0, 7.0, 2.0, 51.0]

# Loop with append
valid_c = []
for value in readings:
    if -50 <= value <= 50:
        valid_c.append(value)
valid_f = []
for value in valid_c:
    valid_f.append(value * 9 / 5 + 32)

# List comprehension
clean_c = [value for value in readings if -50 <= value <= 50]
clean_f = [value * 9 / 5 + 32 for value in clean_c]

# filter() and map()
filtered = list(filter(lambda value: -50 <= value <= 50, readings))
mapped_f = list(map(lambda value: value * 9 / 5 + 32, filtered))

# Minutes are numbered from 1
alarm_minutes = [
    minute for minute, value in enumerate(readings, start=1)
    if -50 <= value <= 50 and not 2 <= value <= 8
]

print("Valid Celsius:", clean_c)
print("Valid Fahrenheit:", [round(x, 1) for x in clean_f])
print("Loop and comprehension match:", valid_c == clean_c)
print("map/filter match:", filtered == clean_c)
print("Alarm minutes:", alarm_minutes)

generator = (value for value in readings if -50 <= value <= 50)
print("List memory:", sys.getsizeof(clean_c))
print("Generator memory:", sys.getsizeof(generator))
