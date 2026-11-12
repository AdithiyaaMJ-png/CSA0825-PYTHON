import time

items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]


def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


def build_join(parts):
    return "".join(p + ";" for p in parts)


def build_fstring(parts):
    lines = [f"{p};" for p in parts]
    return "".join(lines)


a = build_plus(items)
b = build_join(items)
c = build_fstring(items)

print("Same output:", a == b == c)
print("Length:", len(b))

for size in (1_000, 10_000, 200_000):
    sample = items[:size]

    start = time.perf_counter()
    build_plus(sample)
    plus_time = time.perf_counter() - start

    start = time.perf_counter()
    build_join(sample)
    join_time = time.perf_counter() - start

    print(size, "items | +=:", round(plus_time, 4),
          "s | join:", round(join_time, 4), "s")


from io import StringIO

def build_stringio(parts):
    buffer = StringIO()
    for p in parts:
        buffer.write(p)
        buffer.write(";")
    return buffer.getvalue()
