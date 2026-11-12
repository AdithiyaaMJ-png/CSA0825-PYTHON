def ways_redesigned(n):
    if n <= 1:
        return 1

    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(ways_redesigned(5))       # 8
print(ways_redesigned(30))      # 1346269
print(ways_redesigned(1000))    # large integer result
