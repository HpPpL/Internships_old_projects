# tuple - из почти любого объекта делает кортеж.
# print(tuple("12342"))
# for color in ("red", "black", "white"):
#     print(color, "apple")
# range(10,21) range(1,31,2)
# 1
# a = int(input())
# b = int(input())
# for cnt in range(a, b+1):
#     print(cnt, end=' ')
# 2
# a = int(input())
# b = int(input())
# if a < b:
#     for cnt in range(a, b+1):
#         print(cnt, end=' ')
# else:
#     for cnt in range(a, b-1, -1):
#         print(cnt, end=' ')
# 3
# n = int(input())
# print(n * "+___ ")
# s = "|__\ "
# for cnt in range(1, n + 1):
#     print("|", cnt, " / ", sep='', end='')
# print("")
# print(n * s[0:5])
# print(n * "|    ")
# 4
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, sep='', end='')
#     print()
# 5
# numList = list(map(int, input().split()))
# for k in range(0, len(numList), 2):
#     print(numList[k], end=' ')
# 6
# numList = list(map(int, input().split()))
# for k in range(0, len(numList)):
#     if numList[k] % 2 == 0:
#         print(numList[k], end=' ')
# 7
# i = 0
# numList = list(map(int, input().split()))
# for k in range(0, len(numList)):
#     if numList[k] > 0:
#         i += 1
# print(i)
# 8
# numList = list(map(int, input().split()))
# pos = 0
# mx = numList[0]
# for k in range(0, len(numList)):
#     if numList[k] >= mx:
#         mx = numList[k]
#         pos = k
# print(mx, pos)
# 9
# numList = list(map(int, input().split()))
# for k in range(1, len(numList)):
#     if numList[k] > numList[k-1]:
#         print(numList[k], end=' ')
# 10
# numList = list(map(int, input().split()))
# mp = 1001
# for k in range(0, len(numList)):
#     if 0 < numList[k] < mp:
#         mp = numList[k]
# print(mp)
# 11
# n = int(input())
# numList = list(map(int, input().split()))
# x = int(input())
# bm = numList[0]
# for k in range(0, n):
#     if abs(numList[k] - x) < abs(bm - x):
#         bm = numList[k]
# print(bm)
# 12
# numList = list(map(int, input().split()))
# for k in range(0, len(numList), 2):
#     if len(numList) % 2 == 1 and k == len(numList) - 1:
#         break
#     numList[k], numList[k + 1] = numList[k + 1], numList[k]
# print(' '.join(map(str, numList)))
# 13
# numList = list(map(int, input().split()))
# mn = numList[0]
# ps_mn = 0
# mx = numList[0]
# ps_mx = 0
# for k in range(0, len(numList)):
#     if numList[k] < mn:
#         mn = numList[k]
#         ps_mn = k
#     if numList[k] > mx:
#         mx = numList[k]
#         ps_mx = k
# numList[ps_mn], numList[ps_mx] = numList[ps_mx], numList[ps_mn]
# print(' '.join(map(str, numList)))
#
# Методы, не изменяющие список и возвращающие значение:
# count(x) - подсчитывает число вхождений значения x в список. Работает за время O(N)
# index(x) - находит позицию первого вхождения значения x в список. Работает за время O(N)
# index(x, from) - находит позицию первого вхождения значения x в список, начиная с позиции from. Работает за время O(N)
# Методы, не возвращающие значение, но изменяющие список:
# append(x) - добавляет значение x в конец списка
# extend(otherList) - добавляет все содержимое списка otherList в конец списка. В отличие от операции + изменяет объект к которому применен, а не создает новый
# remove(x) - удаляет первое вхождение числа x в список. Работает за время O(N)
# insert(index, x) - вставляет число x в список так, что оно оказывается на позиции index. Число, стоявшее на позиции index и все числа правее него сдвигаются на один вправо. Работает за время O(N)
# reverse() - Разворачивает список (меняет значение по ссылке, а не создает новый список как myList[::-1]). Работает за время O(N)
# Методы, возвращающие значение и изменяющие список:
# pop() - возвращает последний элемент списка и удаляет его
# pop(index) - возвращает элемент списка на позиции index и удаляет его. Работает за время O(N)
