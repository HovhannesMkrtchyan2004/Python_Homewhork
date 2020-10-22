# Ruben 1
# matrix = [[True, False, False],
#           [False, True, False],
#           [True, False, True]]
#
#
# def minesweeper(m):
#     true = [[i, j] for i in range(3) for j in range(3) if m[i][j]]
#     m = [[0 for j in range(3)] for i in range(3)]
#     for i in range(len(true)):
#         x, y = true[i]
#         for j in range(3):
#             for k in range(3):
#                 if abs(j - x) == 1 and abs(k - y) <= 1 or abs(j - x) == 0 and abs(k - y) == 1:
#                     m[j][k] += 1
#     return m
#
#
# print(minesweeper(matrix))


# 2 Ruben
# string = input()
# vow = [string[i:j+1] for i in range(len(string)) if string[i].lower() in 'aeuio' for j in range(i+1, len(string))]
# con = [string[i:j+1] for i in range(len(string)) if string[i].lower() not in 'aeuio' for j in range(i+1,len(string))]
#
# print({el: string.count(el) for el in vow})
# print({el: string.count(el) for el in con})
