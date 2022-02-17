# 1:
# x = int(input())
# y = int(input())
# if x >= y:
#     print(x)
# else:
#     print(y)
# 2:
# x = int(input())
# y = int(input())
# if x > y:
#     print(1)
# elif x < y:
#     print(2)
# else:
#     print(0)
# 3:
# x = int(input())
# y = int(input())
# z = int(input())
# if x >= y and x >= z:
#     print(x)
# elif y >= x and y >= z:
#     print(y)
# else:
#     print(z)
# 4:
# n = int(input())
# if n % 4 == 0 and n % 100 != 0:
#     print('YES')
# elif n % 400 == 0:
#     print('YES')
# else:
#     print('NO')
# 5:
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x1 - x2) < 2 and abs(y1 - y2) < 2:
#     print('YES')
# else:
#     print('NO')
# 6:
# f = int(input())
# lst = int(input())
# if (f - 1) % (1 + lst - f) == 0:
#     print('YES')
# else:
#     print('NO')
# 7:
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (abs(x2 - x1) + abs(y2 - y1)) % 2 == 0:
#     print('YES')
# else:
#     print('NO')
# 8:
# n = int(input())
# m = int(input())
# k = int(input())
# if ((k % n) == 0 or (k % m) == 0) and n * m - k >= 0:
#     print('YES')
# else:
#     print('NO')
# 9:
# n = int(input())
# c = n % 10
# if (c == 0 or 5 <= c <= 9) or 10 < n < 20:
#     print(n, 'korov')
# elif c == 1:
#     print(n, 'korova')
# else:
#     print(n, 'korovy')
# 10:
# n = int(input())
# if n < 0:
#     print(-1)
# elif n == 0:
#     print(0)
# else:
#     print(1)
# 11:
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 >= 0 and y1 >= 0 and x2 >= 0 and y2 >= 0:
#     print('YES')
# elif x1 >= 0 >= y1 and x2 >= 0 >= y2:
#     print('YES')
# elif x1 <= 0 <= y1 >= x2 and y2 >= 0:
#     print('YES')
# elif x1 <= 0 and y1 <= 0 and x2 <= 0 and y2 <= 0:
#     print('YES')
# else:
#     print('NO')
# 12:
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# prv = (abs(x1 - x2) + abs(y1 - y2)) % 2
# if abs(x1 - x2) <= abs(y1 - y2) and prv == 0 and y1 <= y2:
#     print('YES')
# else:
#     print('NO')
# 13:
# a = int(input())
# b = int(input())
# c = int(input())
# if (c**2 == a**2 + b**2) or (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2):
#     if a + b > c and a + c > b and b + c > a:
#         print("rectangular")
#     else:
#         print("impossible")
# elif (c**2 < a**2 + b**2) and (a**2 < b**2 + c**2) and (b**2 < a**2 + c**2):
#     if a + b > c and a + c > b and b + c > a:
#         print("acute")
#     else:
#         print("impossible")
# elif (c**2 > a**2 + b**2) or (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2):
#     if a + b > c and a + c > b and b + c > a:
#         print("obtuse")
#     else:
#         print("impossible")
# else:
#     print("impossible")
# 14:
# a = int(input())
# b = int(input())
# c = int(input())
# flgch = 0
# flgnch = 0
# if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
#     flgch = 1
# if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
#     flgnch = 1
# if flgch * flgnch == 1:
#     print('YES')
# else:
#     print('NO')
# 15:
# a = int(input())
# b = int(input())
# c = int(input())
# if a <= b and a <= c:
#     print(a, end=' ')
#     if b <= c:
#         print(b, c)
#     else:
#         print(c, b)
# elif b <= a and b <= c:
#     print(b, end=' ')
#     if a <= c:
#         print(a, c)
#     else:
#         print(c, a)
# elif c <= a and c <= b:
#     print(c, end=' ')
#     if a <= b:
#         print(a, b)
#     else:
#         print(b, a)
# 16:
# a = int(input())
# b = int(input())
# c = int(input())
# flg = 0
# if a == b:
#     if a == c:
#         print(3)
#     else:
#         print(2)
# elif a == c:
#     if a == b:
#         print(3)
#     else:
#         print(2)
# elif b == c:
#     if a == b:
#         print(3)
#     else:
#         print(2)
# else:
#     print(0)
# 17:
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# if (a <= d and b <= e) or (a <= d and c <= e):
#     print('YES')
# elif (b <= d and a <= e) or (b <= d and c <= e):
#     print('YES')
# elif (c <= d and a <= e) or (c <= d and b <= e):
#     print('YES')
# else:
#     print('NO')
# 18:
# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
# b1 = int(input())
# b2 = int(input())
# b3 = int(input())
# v1 = a1 * a2 * a3
# v2 = b1 * b2 * b3
# if a1 <= b1 and a2 <= b2 and a3 <= b3:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is smaller than the second one')
# elif a1 <= b1 and a2 <= b3 and a3 <= b2:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is smaller than the second one')
# elif a1 <= b2 and a2 <= b1 and a3 <= b3:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is smaller than the second one')
# elif a1 <= b2 and a2 <= b3 and a3 <= b1:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is smaller than the second one')
# elif a1 <= b3 and a2 <= b1 and a3 <= b2:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is smaller than the second one')
# elif a1 <= b3 and a2 <= b2 and a3 <= b1:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is smaller than the second one')
# elif b1 <= a1 and b2 <= a2 and b3 <= a3:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is larger than the second one')
# elif b1 <= a1 and b2 <= a3 and b3 <= a2:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is larger than the second one')
# elif b1 <= a2 and b2 <= a1 and b3 <= a3:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is larger than the second one')
# elif b1 <= a2 and b2 <= a3 and b3 <= a1:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is larger than the second one')
# elif b1 <= a3 and b2 <= a1 and b3 <= a2:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is larger than the second one')
# elif b1 <= a3 and b2 <= a2 and b3 <= a1:
#     if v1 == v2:
#         print('Boxes are equal')
#     else:
#         print('The first box is larger than the second one')
# else:
#     print('Boxes are incomparable')
# 19:
# a = int(input())
# b = int(input())
# c = int(input())
# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# r1 = (a // n1) * (b // n2) * (c // n3)
# r2 = (a // n1) * (b // n3) * (c // n2)
# r3 = (a // n2) * (b // n1) * (c // n3)
# r4 = (a // n2) * (b // n3) * (c // n1)
# r5 = (a // n3) * (b // n1) * (c // n2)
# r6 = (a // n3) * (b // n2) * (c // n1)
# print(max(r1, r2, r3, r4, r5, r6))
# 20:
# k = int(input())
# if k == 1 or k == 2 or k == 4 or k == 7:
#     print('NO')
# else:
#     print('YES')
# 21:
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if c == 0 and d == 0:
#     print('NO')
# elif a == 0 and b == 0:
#     print('INF')
# elif a != 0:
#     if c != 0:
#         if -b / a != -d / c and b % a == 0:
#             print(int(-b / a))
#         else:
#             print('NO')
#     else:
#         print(int(-b / a))
# 22:-
# k = int(input())
# m = int(input())
# n = int(input())
# rez = 2 * n // k
# # k >= n - otvet 2m
# if k > n:
#     print(2 * m)
# elif k<=n:
# if n % k > 0 and k <= n // 2:
#     rez += m
# elif n % k > 0 and k > n // 2:
#     rez += 2 * m
# print(rez)
# 23: -
# 24: -
# 25:
# n = int(input())
# k = 1
# while k ** 2 <= n:
#     print(k ** 2, end=' ')
#     k += 1
# 26:
# n = int(input())
# k = 2
# while k <= n:
#     if n % k == 0:
#         print(k)
#         break
#     k += 1
# 27:
# n = int(input())
# k = 1
# while k <= n:
#     print(k, end=' ')
#     k *= 2
# 28:
# n = int(input())
# while n % 2 == 0:
#     n /= 2
# if n == 1:
#     print('YES')
# else:
#     print('NO')
# 29:
# n = int(input())
# k = 0
# tmp = 1
# while tmp < n:
#     tmp *= 2
#     k += 1
# print(k)
# 30:
# x = int(input())
# y = int(input())
# k = 1
# while x < y:
#     x *= 1.1
#     k += 1
# print(k)
# 31:
# mxm = 0
# x = -1
# while x != 0:
#     x = int(input())
#     if x > mxm:
#         mxm = x
# print(mxm)
# 32:
# n = int(input())
# print(int(n * (n + 1) * (2 * n + 1) / 6))
# 33:
# x = -1
# k = 0
# while x != 0:
#     x = int(input())
#     k += 1
# print(k - 1)
# 34:
# res = 0
# x = -1
# while x != 0:
#     x = int(input())
#     res += x
# print(res)
# 35:
# res = 0
# x = -1
# k = 0
# while x != 0:
#     x = int(input())
#     if x == 0:
#         continue
#     k += 1
#     res += x
# print(res / k)
# 36:
# k = 0
# x = 1
# while x != 0:
#     x = int(input())
#     if x == 0:
#         continue
#     if x % 2 == 0:
#         k += 1
# print(k)
# 37:
# l = int(input())
# n = int(input())
# k = 0
# if n > l:
#     k += 1
# while n != 0:
#     l = n
#     n = int(input())
#     if n > l:
#         k += 1
# print(k)
# 39:
# n = -1
# m = int(input())
# lm = int(input())
# if m < lm:
#     m, lm = lm, m
# while n != 0:
#     n = int(input())
#     if n >= m:
#         lm = m
#         m = n
#     elif n >= lm:
#         lm = n
# print(lm)
# 40:
# mx = -1
# k = 0
# n = -1
# while n != 0:
#     n = int(input())
#     if n > mx:
#         mx = n
#         k = 0
#     if n == mx:
#         k += 1
# print(k)
# 41:
# n = int(input())
# lst = 1
# k = 1
# maxx = 1
# while n != 0:
#     lst = n
#     n = int(input())
#     if n == lst:
#         k += 1
#     else:
#         if k >= maxx:
#             maxx = k
#         k = 1
# print(maxx)
