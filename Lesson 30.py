# Ruben 1
# matrix = [[True, False, False],
#           [False, True, False],
#           [True, False, True]]
#
#
# def minesweeper(m):
#     true = [[i, j] for i in range(len(m)) for j in range(len(m[i])) if m[i][j]]
#     m = [[0 for j in range(len(m[i]))] for i in range(len(m))]
#     for i in range(len(true)):
#         x, y = true[i]
#         for j in range(len(m)):
#             for k in range(len(m[j])):
#                 if abs(j - x) == 1 and abs(k - y) <= 1 or abs(j - x) == 0 and abs(k - y) == 1:
#                     m[j][k] += 1
#     return m
#
#
# for el in minesweeper(matrix):
#     print(el)


# 2 Ruben
# string = input()
# vow = [string[i:j+1] for i in range(len(string)) if string[i].lower() in 'aeuio' for j in range(i, len(string))]
# con = [string[i:j+1] for i in range(len(string)) if string[i].lower() not in 'aeuio' for j in range(i, len(string))]
#
# print({el: string.count(el) for el in vow})
# print({el: string.count(el) for el in con})

# Narek 1
# x = [5, 3, 6, 7, 9]
# i = 2
# qayl = 0
# while i < max(x) + 1:
#     if qayl not in x:
#         qayl += i
#         if qayl > max(x):
#             print(i)
#             break
#         continue
#     qayl = 0
#     i += 1

# Narek 2
# x = input().split('=')
# my_list = []
# lucum = int(x[1])
# count_x = 0
# i = 0
# st = ''
# if x[0][0].isalnum():
#     st += '+'
# while i < len(x[0]):
#     if x[0][i].isalnum() or i == 0:
#         st += x[0][i]
#         i += 1
#     else:
#         my_list.append(st)
#         st = ''
#         st += x[0][i]
#         i += 1
# my_list.append(st)
# for i in range(len(my_list)):
#     if 'x' in my_list[i]:
#         if my_list[i][0] == '+':
#             if my_list[i][1:len(my_list[i]) - 1]:
#                 count_x += int(my_list[i][1:len(my_list[i]) - 1])
#             else:
#                 count_x += 1
#         else:
#             if my_list[i][1:len(my_list[i]) - 1]:
#                 count_x -= int(my_list[i][1:len(my_list[i]) - 1])
#             else:
#                 count_x -= 1
#     else:
#         if my_list[i][0] == '+':
#             lucum -= int(my_list[i][1:])
#         else:
#             lucum += int(my_list[i][1:])
# print('x =', lucum / count_x)
