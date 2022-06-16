(1 + 2) * 3 / 4
dividend = 64 // 7
remainder = 64 % 7
power = 10**5
sqrt2 = 2**0.5

import math

math.sqrt(2)

# numpy
import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 2, 0])

print("a", a)
print("b", b)
print("a+b:", a + b)
print("a*b:", a * b)
print("a/b:", a / b)

a = np.array([[0, 0, 0]])
a_transpose = a.T
print()
print("a", a)
print("a.T")
print(a_transpose)

# outermost dim first
# default type == float
shape = (2, 3)
zer = np.zeros(shape, int)
M1 = np.array(
    [
        [0, 1, 2],
        [2, 3, 4],
    ]
)
# matrix will power using matmul instead of elementwise
M2 = np.mat(
    [
        [0, 1, 2],
        [2, 3, 4],
    ]
)

# first line, first column, first element
M2[0], M2[:, 0], M2[0, 0]

print()
print("zer")
print(zer)
print("M1")
print(M1)
# b will be repeated along the outermost dimensions
# to match M1's shape
print("M1 + b")
print(M1 + b)
print("M1 @ M1.T")
print(M1 @ M1.T)  # matmul
print("M2")
print(M2)

"""
The Fibonacci sequence satisfies a recurrence relation
that can be encoded as a matrix

Fi+2 = Fi+1 + Fi
Fi+1 = Fi+1 + 0

[Fi+2, Fi+1] = M @ [Fi+1, Fi]
[Fi+k+1, Fi+k] = M**k @ [Fi+1, Fi]
"""
M = np.mat(
    [
        [1, 1],
        [1, 0],
    ],
    dtype=object,  # << use python integers
)
n = 100
out = (M**n) @ [1, 0]  # fib1, fib0
print(out)
fib_n = out[0, 1]
