"""
3.6. Performing Complex-Valued Math

Problem
    Your code for interacting with the latest web authentication scheme has encountered a
    singularity and your only solution is to go around it in the complex plane. Or maybe
    you just need to perform some calculations using complex numbers.
Solution
    Complex numbers can be specified using the complex(real, imag) function or by
    floating-point numbers with a j suffix. For example:
"""
import cmath
import math
import numpy as np

a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)

print(a.real)
print(a.imag)

# All of the usual mathematical operators work
print(a+b)
print(a*b)
print(a/b)
print(abs(a))

print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))
print("*" * 20)

arr = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(arr)
print(arr+2)
print(np.sin(arr))

# Python’s standard mathematical functions do not produce complex values by default,
# so it is unlikely that such a value would accidentally show up in your code.
# print(math.sqrt(-1))  # error!

# ...rather
print(cmath.sqrt(-1))  # 1j
