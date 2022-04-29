# input()  # Пропускаем количества, обойдемся без них
# people = map(int, input().split())
# sortedPeople = sorted(enumerate(people), key=lambda x: x[1])
# taxi = map(int, input().split())
# sortedTaxi = sorted(enumerate(taxi), key=lambda x: x[1], reverse=True)
# ans = zip(sortedPeople, sortedTaxi)
# sortedAns = sorted(ans, key=lambda x: x[0][0])
# print(*map(lambda x: x[1][0], sortedAns))
# 1
# print(
#     len(
#         set(
#             map(
#                 int,
#                 input().split()
#             )
#         )
#     )
# )
# 2
# import sys
# print(
#     len(
#         set(
#             sys.stdin.read().split()
#         )
#     )
# )
# 3
# import sys
# print(len(set(sys. stdin.read().split())))
# print(
#     min(
#         filter(
#             lambda x: x % 2 != 0,
#             map(
#                 int,
#                 input().split()
#             )
#         )
#     )
# )
# 4
# print(
#     any(
#         map(
#             lambda x: x == 0,
#             map(int, map(lambda x: input(), range(int(input()))))
#         )
#     )
# )
# 5
# from functools import reduce
# print(
#     reduce(
#         lambda x, y: x * y,
#         map(lambda x: x**5, map(int, input().split()))
#     )
# )
# 6
# print(
#     *list(
#         map(
#             lambda x: x[0] ^ x[1],
#             zip(map(int, input().split()), map(int, input().split()))
#         )
#     )
# )
