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
