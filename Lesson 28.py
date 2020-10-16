# 1 Ruben
# numbers = input()
# n_list = []
# dict_n = dict()
# while numbers != 'End':
#     n_list.append(int(numbers))
#     numbers = input()
#
# for el in n_list:
#     dict_n[el] = n_list.count(el)
#
# print(dict_n)


# 2
# pal = list(input())
# count = 0
# for el in pal:
#     if len(el) % 2:
#         if pal.count(el) == 2:
#             continue
#         else:
#             count += 1
#     else:
#         if pal.count(el) == 2:
#             continue
#         else:
#             count -= 1
#
# print(-1 < count <= 1)


# 3 Narek
# for i in range(1, 101):
#     for j in range(1, 101):
#         k = 1
#         while k < 101 and (k ** j <= i or j ** k <= i):
#             if k ** j == i and j ** k == i:
#                 print(k, j, i)
#             k += 1


# 4
for i in range(1, 5):
    for j in range(i):
        print(i, end='')
    print()
    print()