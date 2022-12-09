# from math import *
import math as m


# y = float(input("Enter any number from 0 to 1: "))


def chaos(x):
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)


# chaos(y)

# n = int(input("Enter exponent: "))
# ans = 1
# for j in range(n):
#     ans = ans * 4
#     print(ans)

print(type(3.0 + 5.0))
print(type(3 + 5))
abs(-2.5)
print(m.sqrt(5))

# print(range(10))
print(3 * 10 / 3)
print(3**3)
print("The square root of 2 is ", m.sqrt(2))
r = int(input("Radius: "))
area = 4 * m.pi * m.pow(r, 2)
print(area)
