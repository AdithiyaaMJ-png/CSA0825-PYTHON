calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received",
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in text.lower().split():
            word = word.strip(".,!?;:")
            if word and word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

print(top(frequencies(calls, STOP), 3))

# Group complaints by district
complaints = [
    ("Vellore", "Seeds delayed"),
    ("Chennai", "Fertiliser price high"),
    ("Vellore", "Water supply issue"),
]
by_district = {}
for district, complaint in complaints:
    by_district.setdefault(district, []).append(complaint)
print("By district:", by_district)
print("District counts:", {d: len(items) for d, items in by_district.items()})
