# 1
# def min4(a, b, c, d):
#     return min(min(a, b), min(c, d))
#
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(min4(a, b, c, d))
# 2
# def IPS(x, y):
# return -1 <= x <= 1 and -1 <= y <= 1
#
#
# x = float(input())
# y = float(input())
# if IPS(x, y):
#     print("YES")
# else:
#     print("NO")
# 3
#
#
# def IPC(x, y, xc, yc, r):
#     eps = 5e-10
#     return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2 + eps
#
#
# x = float(input())
# y = float(input())
# xc = float(input())
# yc = float(input())
# r = float(input())
# if IPC(x, y, xc, yc, r):
#     print("YES")
# else:
#     print("NO")
# 4
#
#
# def MinDivisor(n):
#     k = 2
#     while k <= n ** (1/2):
#         if n % k == 0:
#             return k
#         k += 1
#     return -1
#
#
# n = int(input())
# if MinDivisor(n) != -1:
#     print(MinDivisor(n))
# else:
#     print(n)
# 5
#
#
# def IsPrime(n):
#     k = 2
#     while k <= n ** (1/2):
#         if n % k == 0:
#             return k
#         k += 1
#     return 1
#
#
# n = int(input())
# if IsPrime(n) != 1:
#     print("NO")
# else:
#     print("YES")
# 6
#
#
# def step(a, n):
#     if n != 0:
#         return a * step(a, n-1)
#     else:
#         return 1
#
#
# a = float(input())
# n = int(input())
# print(step(a, n))
# 7
#
#
# def sum(a, b):
#     if b != 0:
#         return 1 + sum(a, b-1)
#     else:
#         return a
#
#
# a = int(input())
# b = int(input())
# print(sum(a, b))
# 8
#
#
# def pow(a, n):
#     if n != 0:
#         if n % 2 == 0:
#             return pow(a, n / 2) ** 2
#         elif n % 2 == 1:
#             return a * pow(a, n - 1)
#     else:
#         return 1
#
#
# a = float(input())
# n = int(input())
# print(pow(a, n))
# 9
#
#
# def gcd(n, m):
#     if n == 0:
#         return m
#     return gcd(m % n, n)
#
#
# n = int(input())
# m = int(input())
# print(n // gcd(n, m), m // gcd(n, m))
# 10
#
#
# def sumr():
#     n = int(input())
#     if n != 0:
#         return n + sumr()
#     else:
#         return 0
#
#
# print(sumr())
# 11
#
#
# def rvrs():
#     n = int(input())
#     if n != 0:
#         rvrs()
#     print(n)
#
#
# rvrs()
