from functools import lru_cache


def fib1(n):
    global counter
    counter += 1
    if n <= 1:
        return n
    return fib1(n - 1) + fib1(n - 2)


@lru_cache
def fib2(n):
    global counter
    counter += 1
    if n <= 1:
        return n
    return fib2(n - 1) + fib2(n - 2)


counter = 0
val = fib1(30)
print(f"fib1(30)={val},    cost: {counter}")

counter = 0
val = fib2(30)
print(f"fib2(30)={val},    cost: {counter}")
