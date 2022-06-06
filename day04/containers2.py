# Comprehensions
## lists can be constructed using a for loop

even_10 = [2 * i for i in range(10)]
print("even_10:\t", even_10)

assert 2**4 == 16  # exponentiation
square_10 = [i**2 for i in range(10)]
print("square_10:\t", square_10)


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


primes_30 = [i for i in range(2, 30) if is_prime(i)]
print("primes_30:\t", primes_30)

print()
## dicts as well

x2_plus3 = {a: a * 2 + 3 for a in range(5)}
print("x2_plus3:\t", x2_plus3)

from_str = {str(a): a for a in range(5)}
print("from_str:\t", from_str)

print()
# Dict iterators
## do not modify dict during iteration (inside for loop)

for k in x2_plus3:
    v = x2_plus3[k]  # get value of key
    print("for:", k, v)

for k in x2_plus3.keys():
    print("for keys:", k)

for v in x2_plus3.values():
    print("for values:", v)

for k, v in x2_plus3.items():
    print("for items:", k, v)
