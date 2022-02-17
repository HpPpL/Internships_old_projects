# 1:
# name = input()
# print('Hello, ', name, '!', sep='')
# n = int(input())
# 2:
# s1 = '   _~_    '
# s2 = '  (o o)   '
# s3 = ' /  V  \  '
# s4 = '/(  _  )\ '
# s5 = '  ^^ ^^   '
# print(s1 * n, sep='')
# print(s2 * n, sep='')
# print(s3 * n, sep='')
# print(s4 * n, sep='')
# print(s5 * n, sep='')
# 3:
# n = int(input())
# k = int(input())
# print(k//n)
# 4:
# n = int(input())
# k = int(input())
# print(k - (k//n) * n)
# 5:
# n = int(input())
# print(2**n)
# 6:
# n = int(input())
# print(n % 10)
# 7:
# n = int(input())
# print(n//10)
# 8:
# n = int(input())
# print((n % 100) // 10)
# 9:
# n = int(input())
# print((n // 100) + ((n % 100) // 10) + (n % 10))
# 10:
# print('A' * 100)
# 11:
# n = int(input())
# n = n % 1440
# print(n // 60, n - (n // 60) * 60)
# 12:
# a = int(input())
# b = int(input())
# n = int(input())
# print((a * n * 100 + b * n) // 100, end=' ')
# print((a * n * 100 + b * n) - ((a * n * 100 + b * n) // 100) * 100)
# 13:
# n = int(input())
# print('The next number for the number ', n, ' is ', n + 1, '.', sep='')
# print('The previous number for the number ', n, ' is ', n - 1, '.', sep='')
# 14:
# n = int(input())
# print(1 - n)
# 15:
# n = int(input())
# print(n + (2 - n % 2))
# 16:
# n = input()
# print(int(n * 100)**2)
# 17:
# v = int(input())
# t = int(input())
# print((v * t) % 109)
# 18: 4265 3602
# n = int(input())
# n = n % 86400
# print(n // 3600, end=':')
# print((n // 60 % 60) // 10, (n // 60 % 60) % 10, sep='', end=':')
# print((n % 60) // 10, (n % 60) % 10, sep='')
# 19:
# h1 = int(input())
# m1 = int(input())
# s1 = int(input())
# h2 = int(input())
# m2 = int(input())
# s2 = int(input())
# print((h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1))
# 20:
# n = int(input())
# m = int(input())
# print((m - 1) // n + 1)
# 21:
# h = int(input())
# a = int(input())
# b = int(input())
# print(1 + (h - 1 - b) // (a - b))
# 22:
# n = int(input())
# print(1 + (n // 1000 - n % 10)**2 + (((n // 100) % 10) - (n // 10) % 10)**2)
# 23:
# a = int(input())
# b = int(input())
# flg = (a // b)
# flg = ((flg + 2) % (flg + 1)) % 2
# print(flg * a + (1 - flg) * b)
# 24:
# a = int(input())
# b = int(input())
# s1 = 'YES'
# s2 = 'NO'
# flg = (a % b)
# flg = ((flg + 2) % (flg + 1)) % 2
# print((1 - flg) * s1 + flg * s2)
# конец!
