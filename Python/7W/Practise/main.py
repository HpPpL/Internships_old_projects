# set {}.
#
# mySet = {1, '2', 2, '1'}
# for elem in mySet:
#     print(elem, end=' ')
#
# mySet.remove(1), но лучше mySet.discard(1).
# Есть добавление - mySet.add(1)
#
# A ^ B - Элементы входят в A | B, но не входят в A & B
# A | B - Объединение множеств
# A & B - Пересечение множеств
# A - B - Множество, элементы которого входят в A, но не входят в B
#
# letters[c] = letters.get(c, 0) + 1
# В гет : c - если нашлось значение, 0 - если нет
# Можно подставлять и другие выражения.
#
# isalpha - проверяет, что все символы строки являются буквами.
#
# isdigit - проверяет, что все символы строки являются цифрами.
#
# isalnum - проверяет, что все символы строки являются буквами или цифрами.
#
# islower - проверяет, что все символы строки являются маленькими буквами.
#
# isupper - проверяет, что все символы строки являются большими буквами.
#
# lstrip - обрезает все пробельные символы в начале строки.
#
# rstrip - обрезает все пробельные символы в конце строки.
#
# strip - обрезает все пробельные символы в начале и конце строки.
#
# 1
# mySet = set(map(int, input().split()))
# print(len(mySet))
# 2
# fSet = set(map(int, input().split()))
# sSet = set(map(int, input().split()))
# rSet = fSet & sSet
# print(*sorted(rSet))
# 3
# myList = list(map(int, input().split()))
# mySet = set()
# rl = len(mySet)
# for elem in myList:
#     mySet.add(elem)
#     if rl < len(mySet):
#         print("NO")
#     else:
#         print("YES")
#     rl = len(mySet)
# 4
# fin = open("input.txt", "r", encoding="utf8")
# lines = fin.readlines()
# myList = []
# for lin in lines:
#     myList += lin.split()
# print(len(set(myList)))
# 5
# n = int(input())
# rSet = set(range(1, n+1))
# while True:
#     str = input()
#     if str == 'HELP':
#         break
#     tmpSet = set(map(int, str.split()))
#     chStr = input()
#     if chStr == 'YES':
#         rSet &= tmpSet
#     elif chStr == 'NO':
#         rSet -= tmpSet
# print(*sorted(rSet))
# 6
# stud = [{input() for i in range(int(input()))} for j in range(int(input()))]
# kbe = set.intersection(*stud)
# kbs = set.union(*stud)
# print(len(kbe), *sorted(kbe), sep='\n')
# print(len(kbs), *sorted(kbs), sep='\n')
# 7
# fin = open("input.txt", "r", encoding="utf8")
# count = {}
# for line in fin:
#     for word in line.split():
#         count[word] = count.get(word, 0) + 1
#         print(count[word] - 1, end=' ')
# 8
# n = int(input())
# sin = {}
# rsin = {}
# for i in range(n):
#     tmpList = list(input().split())
#     sin[tmpList[0]] = tmpList[1]
#     rsin[tmpList[1]] = tmpList[0]
# cw = input()
# if cw in sin:
#     print(sin[cw])
# else:
#     print(rsin[cw])
# 9
# count = {}
# fin = open("input.txt", "r", encoding="utf8")
# lines = fin.readlines()
# for line in lines:
#     for word in line.split():
#         count[word] = count.get(word, 0) + 1
# maxx = max(count.values())
# for w in sorted(count):
#     if count[w] == maxx:
#         print(w)
#         break
# 10
# count = {}
# myList = []
# fin = open("input.txt", "r", encoding="utf8")
# lines = fin.readlines()
# for line in lines:
#     for word in line.split():
#         count[word] = count.get(word, 0) + 1
# for elem in count:
#     myList.append((count[elem], elem))
# rList = sorted(myList, key=lambda elem: (-elem[0], elem[1]))
# for elem in rList:
#     print(elem[1])
# 11
# fin = open("input.txt", "r", encoding="utf8")
# fout = open("output.txt", "w", encoding="utf8")
# lines = fin.readlines()
# canditates = {}
# tmpList = []
# nmb = 0
# for line in lines:
#     canditates[line.strip()] = canditates.get(line.strip(), 0) + 1
#     nmb += 1
# for elem in canditates:
#     tmpList.append((canditates[elem], elem))
# tmpList = sorted(tmpList, key=lambda elem: -elem[0])
# if tmpList[0][0] / nmb > 0.5:
#     print(tmpList[0][1], file=fout)
# else:
#     print(tmpList[0][1], tmpList[1][1], sep='\n', file=fout)
