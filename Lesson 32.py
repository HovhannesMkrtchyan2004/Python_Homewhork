# 1 Ruben
# cell = input()
#
#
# def possible_turns(cell):
#     letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#     return_value = []
#     for i in range(8):
#         for j in range(1, 8):
#             if (abs(letter.index(cell[0]) - i) == 1 and abs(int(cell[1]) - j) == 2) or \
#                     (abs(letter.index(cell[0]) - i) == 2 and abs(int(cell[1]) - j) == 1):
#                 return_value.append(letter[i] + str(j))
#     return return_value
#
#
# print(possible_turns(cell))


# Ruben 2
# chess_board = [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0,'Q', 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0]
# ]
#
#
# def add_queen_possible_steps(chess_board):
#     flag = False
#     for i in range(8):
#         for j in range(8):
#             if 'Q' == chess_board[i][j]:
#                 q = [i + 1, j + 1]
#                 flag = True
#                 break
#         if flag:
#             break
#     print(q)
#     for i in range(1, 9):
#         for j in range(1, 9):
#             if chess_board[i - 1][j - 1] != 1 and (abs(q[0] - i) == abs(q[1] - j) or i == q[0] or j == q[1]):
#                 chess_board[i - 1][j - 1] = 'x'
#     chess_board[q[0] - 1][q[1] - 1] = 'Q'
#
#     for i in range(8):
#         for j in range(8):
#             if chess_board[i][j] == 'x':
#                 k = i
#                 k_2 = j
#                 while k < 8 and k_2 < 8 and abs(q[0] - 1 - i) == abs(q[1] - 1 - j):
#                     if k == q[0] - 1 and k_2 == q[0] - 1:
#                         break
#                     elif k < q[0] - 1 and k_2 < q[1] - 1:
#                         if chess_board[k][k_2] == 1:
#                             chess_board[i][j] = 0
#                             break
#                         k += 1
#                         k_2 += 1
#                         continue
#                     elif k > q[0] - 1 and k_2 > q[1] - 1:
#                         if chess_board[k][k_2] == 1:
#                             chess_board[i][j] = 0
#                             break
#                         k -= 1
#                         k_2 -= 1
#                         continue
#                     elif k < q[0] - 1 and k_2 > q[1] - 1:
#                         if chess_board[k][k_2] == 1:
#                             chess_board[i][j] = 0
#                             break
#                         k += 1
#                         k_2 -= 1
#                         continue
#                     elif k > q[0] - 1 and k_2 < q[1] - 1:
#                         if chess_board[k][k_2] == 1:
#                             chess_board[i][j] = 0
#                             break
#                         k -= 1
#                         k_2 += 1
#                         continue
#                     break
#                 k = j
#                 while k < 8 and i == q[0] - 1:
#                     if k == q[1] - 1:
#                         break
#                     elif k < q[1] - 1:
#                         if chess_board[i][k] == 1:
#                             chess_board[i][j] = 0
#                             break
#                         k += 1
#                     else:
#                         if chess_board[i][k] == 1:
#                             chess_board[i][j] = 0
#                             break
#                         k -= 1
#                 k = i
#                 while k < 8 and j == q[1] - 1:
#                     if k == q[0] - 1:
#                         break
#                     elif k < q[0] - 1:
#                         if chess_board[k][j] == 1:
#                             chess_board[i][j] = 0
#                             break
#                         k += 1
#                     else:
#                         if chess_board[k][j] == 1:
#                             chess_board[i][j] = 0
#                             break
#                         k -= 1
#
#                 # for el in chess_board:
#                 #     print(*el)
#                 # print()
#     return chess_board
#
#
# for el in add_queen_possible_steps(chess_board):
#     print(*el)

# 1 Narek
# a = input()
# b = input()
#
# letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#
# print((letter.index(a[0]) + 1 + letter.index(b[0]) + 1 + int(a[1]) + int(b[1])) % 2 == 0)

# 2 Narek
chess_board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['r', 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0,0, 0, 0, 0, 0, 0],
    [0, 'q', 0, 0, 0, 0, 0, 0],
    ['ek',0, 0, 0, 0, 0, 0, 'r']
]


def mat(chess_board):
    r_1 = []
    r_2 = []
    q = []
    ek = []
    for i in range(8):
        for j in range(8):
            if 'r' == chess_board[i][j] and len(r_1) == 0:
                r_1 = [i, j]
            elif 'r' == chess_board[i][j]:
                r_2 = [i, j]
            if 'q' == chess_board[i][j]:
                q = [i, j]
            if 'ek' == chess_board[i][j]:
                ek = [i, j]
    x = [r_1[0], r_2[0], q[0]]
    y = [r_1[1], r_2[1], q[1]]
    flag = False
    for i in range(2):
        if (ek[0] == r_1[0] and not (ek[1] == r_1[1])) or (ek[0] == r_2[0] and not (ek[1] == r_2[1])) or (
                ek[0] == q[0] and not (ek[1] == q[1])) or \
                (ek[1] == r_1[1] and not (ek[0] == r_1[0])) or (ek[1] == r_2[1] and not (ek[0] == r_2[0])) or (
                ek[1] == q[1] and not (ek[0] == q[0])) or \
                (abs(ek[0] - q[0]) == abs(ek[1] - q[1]) and ek[1] == q[1] and not (ek[0] == q[0])):
            x = ek
            if x[0] + 1 < 8 and x[1] + 1 < 8:
                x[0], x[1] = x[0] + 1, x[1] + 1
                if not((x[0] == r_1[0] and not (x[1] == r_1[1])) or (x[0] == r_2[0] and not (x[1] == r_2[1])) or (
                        x[0] == q[0] and not (x[1] == q[1])) or \
                        (x[1] == r_1[1] and not (x[0] == r_1[0])) or (x[1] == r_2[1] and not (x[0] == r_2[0])) or (
                                x[1] == q[1] and not (x[0] == q[0])) or \
                        (abs(x[0] - q[0]) == abs(x[1] - q[1]) and x[1] == q[1] and not (x[0] == q[0]))):
                    flag = True
            x = ek
            if x[0] - 1 > 0 and x[1] - 1 > 0:
                x[0], x[1] = x[0] - 1, x[1] - 1
                if not((x[0] == r_1[0] and not (x[1] == r_1[1])) or (x[0] == r_2[0] and not (x[1] == r_2[1])) or (
                        x[0] == q[0] and not (x[1] == q[1])) or \
                        (x[1] == r_1[1] and not (x[0] == r_1[0])) or (x[1] == r_2[1] and not (x[0] == r_2[0])) or (
                                x[1] == q[1] and not (x[0] == q[0])) or \
                        (abs(x[0] - q[0]) == abs(x[1] - q[1]) and x[1] == q[1] and not (x[0] == q[0]))):
                    flag = True
            x = ek
            if x[0] - 1 > 0 and x[1] + 1 < 8:
                x[0], x[1] = x[0] - 1, x[1] + 1
                if not((x[0] == r_1[0] and not (x[1] == r_1[1])) or (x[0] == r_2[0] and not (x[1] == r_2[1])) or (
                        x[0] == q[0] and not (x[1] == q[1])) or \
                        (x[1] == r_1[1] and not (x[0] == r_1[0])) or (x[1] == r_2[1] and not (x[0] == r_2[0])) or (
                                x[1] == q[1] and not (x[0] == q[0])) or \
                        (abs(x[0] - q[0]) == abs(x[1] - q[1]) and x[1] == q[1] and not (x[0] == q[0]))):
                    flag = True
            x = ek
            if x[0] + 1 < 8 and x[1] - 1 > 0:
                x[0], x[1] = x[0] + 1, x[1] - 1
                x[0] += 1
                if not((x[0] == r_1[0] and not (x[1] == r_1[1])) or (x[0] == r_2[0] and not (x[1] == r_2[1])) or (
                        x[0] == q[0] and not (x[1] == q[1])) or \
                        (x[1] == r_1[1] and not (x[0] == r_1[0])) or (x[1] == r_2[1] and not (x[0] == r_2[0])) or (
                                x[1] == q[1] and not (x[0] == q[0])) or \
                        (abs(x[0] - q[0]) == abs(x[1] - q[1]) and x[1] == q[1] and not (x[0] == q[0]))):
                    flag = True
            x = ek
            if x[0] + 1 < 8:
                x[0] += 1
                if not((x[0] == r_1[0] and not (x[1] == r_1[1])) or (x[0] == r_2[0] and not (x[1] == r_2[1])) or (
                        x[0] == q[0] and not (x[1] == q[1])) or \
                        (x[1] == r_1[1] and not (x[0] == r_1[0])) or (x[1] == r_2[1] and not (x[0] == r_2[0])) or (
                                x[1] == q[1] and not (x[0] == q[0])) or \
                        (abs(x[0] - q[0]) == abs(x[1] - q[1]) and x[1] == q[1] and not (x[0] == q[0]))):
                    flag = True
            x = ek
            if x[0] - 1 > 0:
                x[0] -= 1
                if not((x[0] == r_1[0] and not (x[1] == r_1[1])) or (x[0] == r_2[0] and not (x[1] == r_2[1])) or (
                        x[0] == q[0] and not (x[1] == q[1])) or \
                        (x[1] == r_1[1] and not (x[0] == r_1[0])) or (x[1] == r_2[1] and not (x[0] == r_2[0])) or (
                                x[1] == q[1] and not (x[0] == q[0])) or \
                        (abs(x[0] - q[0]) == abs(x[1] - q[1]) and x[1] == q[1] and not (x[0] == q[0]))):
                    flag = True
            if x[1] - 1 > 0:
                x[1] -= 1
                if not((x[0] == r_1[0] and not (x[1] == r_1[1])) or (x[0] == r_2[0] and not (x[1] == r_2[1])) or (
                        x[0] == q[0] and not (x[1] == q[1])) or \
                        (x[1] == r_1[1] and not (x[0] == r_1[0])) or (x[1] == r_2[1] and not (x[0] == r_2[0])) or (
                                x[1] == q[1] and not (x[0] == q[0])) or \
                        (abs(x[0] - q[0]) == abs(x[1] - q[1]) and x[1] == q[1] and not (x[0] == q[0]))):
                    flag = True
            if x[1] + 1 < 8:
                x[1] += 1
                if not((x[0] == r_1[0] and not (x[1] == r_1[1])) or (x[0] == r_2[0] and not (x[1] == r_2[1])) or (
                        x[0] == q[0] and not (x[1] == q[1])) or \
                        (x[1] == r_1[1] and not (x[0] == r_1[0])) or (x[1] == r_2[1] and not (x[0] == r_2[0])) or (
                                x[1] == q[1] and not (x[0] == q[0])) or \
                        (abs(x[0] - q[0]) == abs(x[1] - q[1]) and x[1] == q[1] and not (x[0] == q[0]))):
                    flag = True

    print(flag)


mat(chess_board)
