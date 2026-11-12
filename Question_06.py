timetable = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:10"),
            ("Katpadi", "08:00", "08:05"),
            ("Bengaluru", "11:00", "11:10")
        ],
        "days": {"Mon", "Wed", "Fri"}
    },
    "12602": {
        "name": "West Coast Express",
        "stops": [
            ("Chennai", "07:00", "07:15"),
            ("Katpadi", "09:00", "09:05"),
            ("Coimbatore", "14:00", "14:10")
        ],
        "days": {"Tue", "Thu", "Sat"}
    },
    "12603": {
        "name": "Intercity Express",
        "stops": [
            ("Bengaluru", "06:30", "06:40"),
            ("Katpadi", "09:30", "09:35"),
            ("Chennai", "12:00", "12:10")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri"}
    },
    "12604": {
        "name": "Hill Express",
        "stops": [
            ("Chennai", "08:00", "08:10"),
            ("Salem", "12:00", "12:05"),
            ("Coimbatore", "15:00", "15:10")
        ],
        "days": {"Sun"}
    },
    "12605": {
        "name": "Night Express",
        "stops": [
            ("Bengaluru", "20:00", "20:10"),
            ("Katpadi", "23:00", "23:05"),
            ("Chennai", "02:00", "02:10")
        ],
        "days": {"Mon", "Wed", "Fri"}
    }
}

station, day = "Katpadi", "Mon"
matches = []
for number, train in timetable.items():
    if day in train["days"]:
        for stop, arrival, departure in train["stops"]:
            if stop == station:
                matches.append((departure, number, train["name"], arrival))

matches.sort(key=lambda item: item[0])
print("Trains at", station, "on", day)
for departure, number, name, arrival in matches:
    print(number, name, "Arrival:", arrival, "Departure:", departure)

# Build station -> list of train numbers index
station_index = {}
for number, train in timetable.items():
    for stop, arrival, departure in train["stops"]:
        station_index.setdefault(stop, []).append(number)

print("Index for Katpadi:", station_index.get("Katpadi", []))
print("Unknown station:", station_index.get("Madurai", []))
