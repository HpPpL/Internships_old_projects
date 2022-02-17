# T1:
# x = 0.1
# print('{0:.25f}'.format(x)) - вывод 25 знаков числа x
# T2:
# print(float(123.24).as_integer_ratio())-как представляется число в виде дроби
# T3:
# import math
# print(math.floor(-2.5))
# print(math.ceil(-2.5))
# или
# from math import floor, ceil
# print(floor(-2.5))
# print(ceil(-2.5))
# 1:
# a = float(input())
# b = float(input())
# c = float(input())
# p = float((a + b + c) / 2)
# print('{0:.10f}'.format((p * (p - a) * (p - b) * (p - c)) ** (1 / 2)))
# 2:
# n = int(input())
# res = float(0)
# k = 1
# while k <= n:
#     res += 1 / (k ** 2)
#     k += 1
# print('{0:.10f}'.format(res))
# 3:
# from math import floor
# x = float(input())
# print('{0:.10f}'.format(x - floor(x)))
# 4:
# from math import floor, trunc
# x = float(input())
# print(format(trunc(x)), round(100 * (x - floor(x))))
# 5:
# from math import floor, trunc, ceil
# x = float(input())
# eps = 5e-11
# if x - (trunc(x)) >= 0.5 - eps:
#     print(ceil(x))
# else:
#     print(floor(x))
# 6:
# from math import floor, trunc
# p = int(input())
# x = int(input())
# y = int(input())
# eps = 5e-10
# kp = (100 * x + y) * (1 + p / 100)
# if abs(round(kp) - kp) <= eps:
#     kp = round(kp)
#     rub = int(kp // 100)
#     kp = kp - rub * 100
#     print(rub, floor(kp))
# else:
#     kp = trunc(kp)
#     rub = int(kp // 100)
#     kp = kp - rub * 100
#     print(rub, floor(kp))
# 7:
# from math import floor
# a = float(input())
# b = float(input())
# c = float(input())
# eps = 5e-10
# if b ** 2 - 4 * a * c <= 0 - eps:
#     print()
# elif abs(b ** 2 - 4 * a * c) <= eps:
#     print('{0:.10f}'.format((-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)))
# elif b ** 2 - 4 * a * c >= 0 + eps:
#     x = (-b + (b ** 2 - 4 * a * c) ** (1 / 2))/(2 * a)
#     y = (-b - (b ** 2 - 4 * a * c) ** (1 / 2))/(2 * a)
#     print('{0:.10f}'.format(min(x, y)), end=' ')
#     print('{0:.10f}'.format(max(x, y)), end=' ')
# 8:
# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())
# f = float(input())
# x = (d * e - b * f) / (a * d - b * c)
# if a == 0:
#     y = e / b
# elif c == 0:
#     y = f / d
# else:
#     if b != 0:
#         y = (e - a * x) / b
#     elif d != 0:
#         y = (f - c * x) / d
# print('{0:.10f}'.format(x), '{0:.10f}'.format(y))
# 9:
# s = input()
# print(s[2])
# print(s[-2])
# print(s[0:5])
# print(s[0:(len(s) - 2)])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[-1::-2])
# print(len(s))
# 10:
# s = input()
# sr = s[::-1]
# fp = s.find('f')
# lp = len(s) - sr.find('f') - 1
# if fp == -1:
#     print()
# elif fp == lp:
#     print(fp)
# elif fp != lp:
#     print(fp, lp)
# 11:
# s = input()
# sr = s[::-1]
# fp = s.find('h')
# lp = len(s) - sr.find('h') - 1
# print(s[0:fp], s[(lp + 1):], sep='')
# 12:
# s = input()
# pos1 = 0
# pos2 = 0
# if s.find('f') == -1:
#     print(-2)
# else:
#     pos1 = s.find('f') + 1
#     pos2 = s.find('f', pos1)
#     if pos2 == -1:
#         print(-1)
#     else:
#         print(pos2)
# 13:
# s = input()
# pos = s.find(' ')
# print(s[pos + 1:len(s)], s[0:pos])
# 14:
# s = input()
# s.count(' ')
# print(s.count(' ') + 1)
# 15:
# s = input()
# print(s.replace('1', 'one'))
# 16:
# s = input()
# print(s.replace('@', ''))
