from functools import lru_cache

calls = 0

def ways_naive(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


calls = 0
print("naive:", ways_naive(25), "calls =", calls)

calls = 0
ways_memo.cache_clear()
print("memo :", ways_memo(25), "calls =", calls)


def ways_loop(n):
    if n <= 1:
        return 1

    previous, current = 1, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous

print(ways_loop(5))       # 8
print(ways_loop(1000))    # works without recursion
