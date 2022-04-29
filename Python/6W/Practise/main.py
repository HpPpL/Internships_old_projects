# sort - Изменяет оригинал.
# sorted-создает копию и сортирует все. Буквы, цифры. Передать можно что угодно
# def (*args)
# def (first, others)
# fin = open('input.txt', 'r', encoding='utf8')
# a = int(fin.readline()) - скан строки, до конца.
# b = int(fin.readline())
# lines = fin.readlines() - лист всех строк.
# lines[0].strip() - обрубает пробелы, табуляции и т.д..
# s = fin.read() - весь файлик в колбаску.
# print(sum(map(int, fin.readlines())), file = fout) fout - файл для вывода.
# fout.close() - закрыть файл.
# grades = [0] * 11
# 1
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
#
# def merge(A, B):
#         C = []
#         i, j = 0, 0
#         for k in range(len(A) + len(B)):
#             if i < len(A) and j < len(B):
#                 if A[i] < B[j]:
#                     C.append(A[i])
#                     i += 1
#                 else:
#                     C.append(B[j])
#                     j += 1
#             elif i < len(A):
#                 C.append(A[i])
#                 i += 1
#             elif j < len(B):
#                 C.append(B[j])
#                 j += 1
#         return C
#
#
# print(*merge(a, b))
# 2
# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# print(*a)
# 3
# s, n = map(int, input().split())
# a = []
# for k in range(0, n):
#     a.append(int(input()))
# a.sort()
# tmp = 0
# i = 0
# while s >= 0 and i < n:
#     if s - a[i] >= 0:
#         s -= a[i]
#         tmp += 1
#     i += 1
# print(tmp)
# 4
# n = int(input())
# hl = list(map(int, input().split()))
# for i in range(n):
#     hl[i] = [hl[i], i + 1, 0]
# hl.sort()
#
# m = int(input())
# bl = list(map(int, input().split()))
# for i in range(m):
#     bl[i] = [bl[i], i + 1, 0]
# bl.sort()
#
# spos = 0
# for i in range(n):
#     indx = 0
#     minn = 10e+9
#     for j in range(spos, m):
#         tmp = abs(hl[i][0] - bl[j][0])
#         if tmp < minn:
#             indx = j
#             minn = tmp
#             hl[i][2] = bl[j][1]
#         else:
#             break
#     spos = indx
#
# hl.sort(key=lambda indx: indx[1])
# for i in range(n):
#     print(hl[i][2], end=' ')
# 5
# fin = open('input.txt', 'r', encoding='utf8')
# fout = open('output.txt', 'w', encoding='utf8')
# lines = fin.readlines()
# db = []
# for i in range(0, len(lines)):
#     tmpData = lines[i].split()
#     db.append([tmpData[0], tmpData[1], int(tmpData[3])])
# db.sort(key=lambda db: db[0])
# for i in range(0, len(db)):
#     print(db[i][0], db[i][1], db[i][2], file=fout)
# fin.close()
# 6
#
#
# def CountSort(A):
#     nmb = [0] * 101
#     for number in A:
#         nmb[number] += 1
#     for nowNmb in range(0, 101):
#         print((str(nowNmb) + ' ') * nmb[nowNmb], end='')
#
#
# num = list(map(int, input().split()))
# CountSort(num)
# 7
# n = int(input())
# db = []
# for i in range(n):
#     tmpData = input().split()
#     db.append([tmpData[0], int(tmpData[1])])
# db.sort(key=lambda db: db[1])
# for i in range(n):
#     print(db[n-1-i][0])
# 8. Тут будет 2 балдежных момента : rsplit ; z.split()[-3:].
#
#
# def SumBal(z):
#     tmpLst = z.rsplit(maxsplit=3)
#     if int(tmpLst[1]) >= 40 and int(tmpLst[2]) >= 40 and int(tmpLst[3]) >= 40:
#         return int(tmpLst[1]) + int(tmpLst[2]) + int(tmpLst[3])
#     else:
#         return -1
#
#
# fin = open('input.txt', 'r', encoding='utf8')
# fout = open('output.txt', 'w', encoding='utf8')
# k = int(fin.readline())
# lines = fin.readlines()
# db = [0] * 301
# ne_proh = 0
#
# for s in lines:
#     tmpStr = s[0:len(s)-1]
#     tmpZn = SumBal(tmpStr)
#     if tmpZn != -1:
#         db[tmpZn] += 1
#     else:
#         ne_proh += 1
#
# cntrl = 0
# pr_ball = 301
# i = 300
#
# while i >= 120 and cntrl + db[i] <= k:
#     if db[i] != 0:
#         pr_ball = i
#         cntrl += db[i]
#     i -= 1
# if i == 119 and cntrl <= k:
#     print(0, file=fout)
# elif pr_ball == 301 and db[i] > k:
#     print(1, file=fout)
# else:
#     print(pr_ball, file=fout)
#
# fin.close()
# fout.close()
#