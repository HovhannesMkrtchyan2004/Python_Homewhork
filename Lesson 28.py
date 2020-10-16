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
#     if not pal.count(el) == 2 and len(el) % 2:
#         count += 1
#     elif not pal.count(el) == 2 and len(el) % 2 == 0:
#         count -= 1
# print(-1 < count <= 1)


# 3 Narek
# for i in range(1, 101):
#     for j in range(1, 101):
#         if i ** j == j ** i and i ** j <= 100:
#             print(i, j, i ** j)

# 4
# for i in range(1, 5):
#     for j in range(i):
#         print(i, end='')
#     print()
#     print()
