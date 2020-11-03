# 1 Narek
def tree(list_1):
    tree_coord = []
    for i in range(len(list_1)):
        if list_1[i] == -1:
            tree_coord.append(i)
    for i in range(len(list_1)):
        if list_1[i] == -1:
            list_1.append(list_1.pop(i))
    for _ in range(len(tree_coord)):
        list_1.pop()
    list_1.sort()
    for el in tree_coord:
        list_1.insert(el, -1)
    return list_1


print(tree([2, -1, 1, 5, 4, -1, 3]))
#
#
# def sort_and_push_tree_cords(list_1):
#     tree_cord = get_tree_coord(list_1)[0]
#     my_list = get_tree_coord(list_1)[1]
#     for _ in range(len(tree_cord)):
#         my_list.pop()
#     my_list.sort()
#     for el in tree_cord:
#         my_list.insert(el, -1)
#     return my_list

# 2 Narek
# my_list = [[10, 'f', 'w'],
#            [0, 'w', 0],
#            [0, 'w', 10]]
#
#
# def get_coord_enimals(board):
#     flag = False
#     enimal_1 = list()
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if not (enimal_1) and board[i][j] == 10:
#                 enimal_1 = [i, j]
#             elif enimal_1 and board[i][j] == 10:
#                 enimal_2 = [i, j]
#                 flag = True
#                 break
#     if flag:
#         return [enimal_1, enimal_2]
#
#     else:
#         return [enimal_1]
#
#
# def game(board):
#     len_ = len(get_coord_enimals(board))
#     if len_ == 2:
#         enimal_1, enimal_2 = get_coord_enimals(board)
#         count = 0
#     else:
#         enimal_1 = get_coord_enimals(board)[0]
#         count = 1
#     while count != 2:
#         if len_ == 2 and (abs(enimal_1[0] - enimal_2[0]) == 1 or abs(enimal_1[1] - enimal_2[1]) == 1) and count == 0:
#             if board[enimal_1[0]][enimal_1[1]] - board[enimal_2[0]][enimal_2[1]] == 0:
#                 board[enimal_1[0]][enimal_1[1]], board[enimal_2[0]][enimal_2[1]] = 'd', 'd'
#                 return board
#             elif board[enimal_1[0]][enimal_1[1]] - board[enimal_2[0]][enimal_2[1]] < 0:
#                 board[enimal_2[0]][enimal_2[1]] -= board[enimal_1[0]][enimal_1[1]]
#                 board[enimal_1[0]][enimal_1[1]] = 'd'
#                 count += 1
#             elif board[enimal_1[0]][enimal_1[1]] - board[enimal_2[0]][enimal_2[1]] > 0:
#                 board[enimal_1[0]][enimal_1[1]] -= board[enimal_2[0]][enimal_2[1]]
#                 board[enimal_2[0]][enimal_2[1]] = 'd'
#                 count += 1
#         elif len_ == 1 or abs(enimal_1[0] - enimal_2[0]) > 1 or abs(enimal_1[1] - enimal_2[1]) > 1 or count == 1:
#             if board[enimal_1[0]][enimal_1[1]] != 'd':
#                 if enimal_1[1] + 1 < len(board[enimal_1[0]]) and board[enimal_1[0]][enimal_1[1] + 1] == 'f':
#                     board[enimal_1[0]][enimal_1[1]] += 1
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] + 1] = 0, board[enimal_1[0]][
#                         enimal_1[1]]
#                     enimal_1[1] += 1
#                 elif enimal_1[1] + 1 < len(board[enimal_1[0]]) and board[enimal_1[0]][enimal_1[1] + 1] == 'w':
#                     board[enimal_1[0]][enimal_1[1]] += 0.5
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] + 1] = 0, board[enimal_1[0]][
#                         enimal_1[1]]
#                     enimal_1[1] += 1
#                 elif enimal_1[1] - 1 > 0 and board[enimal_1[0]][enimal_1[1] - 1] == 'f':
#                     board[enimal_1[0]][enimal_1[1]] += 1
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] - 1] = 0, board[enimal_1[0]][
#                         enimal_1[1]]
#                     enimal_1[1] -= 1
#                 elif enimal_1[1] - 1 > 0 and board[enimal_1[0]][enimal_1[1] - 1] == 'w':
#                     board[enimal_1[0]][enimal_1[1]] += 0.5
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] - 1] = 0, board[enimal_1[0]][
#                         enimal_1[1]]
#                     enimal_1[1] -= 1
#                 elif enimal_1[0] + 1 < len(board) and board[enimal_1[0] + 1][enimal_1[1]] == 'f':
#                     board[enimal_1[0]][enimal_1[1]] += 1
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1]] = 0, board[enimal_1[0]][
#                         enimal_1[1]]
#                     enimal_1[0] += 1
#                 elif enimal_1[0] + 1 > len(board) and board[enimal_1[0] + 1][enimal_1[1]] == 'w':
#                     board[enimal_1[0]][enimal_1[1]] += 0.5
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1]] = 0, board[enimal_1[0]][
#                         enimal_1[1]]
#                     enimal_1[0] += 1
#                 elif enimal_1[0] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1]] == 'f':
#                     board[enimal_1[0]][enimal_1[1]] += 1
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1]] = 0, board[enimal_1[0]][
#                         enimal_1[1]]
#                     enimal_1[0] -= 1
#                 elif enimal_1[0] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1]] == 'w':
#                     board[enimal_1[0]][enimal_1[1]] += 0.5
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1]] = 0, board[enimal_1[0]][
#                         enimal_1[1]]
#                     enimal_1[0] -= 1
#                 elif enimal_1[0] + 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
#                         board[enimal_1[0] + 1][enimal_1[1] + 1] == 'f':
#                     board[enimal_1[0]][enimal_1[1]] += 1
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] + 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                     enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] + 1
#                 elif enimal_1[0] + 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
#                         board[enimal_1[0] + 1][enimal_1[1] + 1] == 'w':
#                     board[enimal_1[0]][enimal_1[1]] += 0.5
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] + 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                     enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] + 1
#                 elif enimal_1[0] - 1 > 0 and enimal_1[1] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1] - 1] == 'f':
#                     board[enimal_1[0]][enimal_1[1]] += 1
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] - 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                     enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] - 1
#                 elif enimal_1[0] - 1 > 0 and enimal_1[1] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1] - 1] == 'w':
#                     board[enimal_1[0]][enimal_1[1]] += 0.5
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] - 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                     enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] - 1
#                 elif enimal_1[0] + 1 < len(board) and enimal_1[1] - 1 > 0 and board[enimal_1[0] + 1][
#                     enimal_1[1] - 1] == 'f':
#                     board[enimal_1[0]][enimal_1[1]] += 1
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] - 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                     enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] + 1
#                 elif enimal_1[0] + 1 < len(board) and enimal_1[1] - 1 > 0 and board[enimal_1[0] + 1][
#                     enimal_1[1] - 1] == 'w':
#                     board[enimal_1[0]][enimal_1[1]] += 0.5
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] - 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                     enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] - 1
#                 elif enimal_1[0] - 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
#                         board[enimal_1[0] - 1][enimal_1[1] + 1] == 'f':
#                     board[enimal_1[0]][enimal_1[1]] += 1
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] + 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                     enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] + 1
#                 elif enimal_1[0] - 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
#                         board[enimal_1[0] - 1][enimal_1[1] + 1] == 'w':
#                     board[enimal_1[0]][enimal_1[1]] += 0.5
#                     board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] + 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                     enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] + 1
#                 else:
#                     if enimal_1[1] + 1 < len(board[enimal_1[0]]):
#                         board[enimal_1[0]][enimal_1[1]] -= 1
#                         board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] + 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                         enimal_1[1] += 1
#                         if board[enimal_1[0]][enimal_1[1]] <= 0:
#                             board[enimal_1[0]][enimal_1[1]] = 'd'
#                             count += 1
#                     else:
#                         board[enimal_1[0]][enimal_1[1]] -= 1
#                         board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] - 1] = 0, \
#                                                                                                board[enimal_1[0]][
#                                                                                                    enimal_1[1]]
#                         enimal_1[1] -= 1
#                         if board[enimal_1[0]][enimal_1[1]] <= 0:
#                             board[enimal_1[0]][enimal_1[1]] = 'd'
#                             count += 1
#             if len_ == 2 and board[enimal_2[0]][enimal_2[1]] != 'd':
#                 if enimal_2[1] + 1 < len(board[enimal_2[0]]) and board[enimal_2[0]][enimal_2[1] + 1] == 'f':
#                     board[enimal_2[0]][enimal_2[1]] += 1
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] + 1] = 0, board[enimal_2[0]][
#                         enimal_2[1]]
#                     enimal_2[1] += 1
#                 elif enimal_2[1] + 1 < len(board[enimal_2[0]]) and board[enimal_2[0]][enimal_2[1] + 1] == 'w':
#                     board[enimal_2[0]][enimal_2[1]] += 0.5
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] + 1] = 0, board[enimal_2[0]][
#                         enimal_2[1]]
#                     enimal_2[1] += 1
#                 elif enimal_2[1] - 1 > 0 and board[enimal_2[0]][enimal_2[1] - 1] == 'f':
#                     board[enimal_2[0]][enimal_2[1]] += 1
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] - 1] = 0, board[enimal_2[0]][
#                         enimal_2[1]]
#                     enimal_2[1] -= 1
#                 elif enimal_2[1] - 1 > 0 and board[enimal_2[0]][enimal_2[1] - 1] == 'w':
#                     board[enimal_2[0]][enimal_2[1]] += 0.5
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] - 1] = 0, board[enimal_2[0]][
#                         enimal_2[1]]
#                     enimal_2[1] -= 1
#                 elif enimal_2[0] + 1 < len(board) and board[enimal_2[0] + 1][enimal_2[1]] == 'f':
#                     board[enimal_2[0]][enimal_2[1]] += 1
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1]] = 0, board[enimal_2[0]][
#                         enimal_2[1]]
#                     enimal_2[0] += 1
#                 elif enimal_2[0] + 1 > len(board) and board[enimal_2[0] + 1][enimal_2[1]] == 'w':
#                     board[enimal_2[0]][enimal_2[1]] += 0.5
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1]] = 0, board[enimal_2[0]][
#                         enimal_2[1]]
#                     enimal_2[0] += 1
#                 elif enimal_2[0] - 1 > 0 and board[enimal_2[0] - 1][enimal_2[1]] == 'f':
#                     board[enimal_2[0]][enimal_2[1]] += 1
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1]] = 0, board[enimal_2[0]][
#                         enimal_2[1]]
#                     enimal_2[0] -= 1
#                 elif enimal_2[0] - 1 > 0 and board[enimal_2[0] - 1][enimal_2[1]] == 'w':
#                     board[enimal_2[0]][enimal_2[1]] += 0.5
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1]] = 0, board[enimal_2[0]][
#                         enimal_2[1]]
#                     enimal_2[0] -= 1
#                 elif enimal_2[0] + 1 < len(board) and enimal_2[1] + 1 < len(board[enimal_2[0]]) and \
#                         board[enimal_2[0] + 1][enimal_2[1] + 1] == 'f':
#                     board[enimal_2[0]][enimal_2[1]] += 1
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1] + 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                     enimal_2[0], enimal_2[1] = enimal_2[0] + 1, enimal_2[1] + 1
#                 elif enimal_2[0] + 1 < len(board) and enimal_2[1] + 1 < len(board[enimal_2[0]]) and \
#                         board[enimal_2[0] + 1][enimal_2[1] + 1] == 'w':
#                     board[enimal_2[0]][enimal_2[1]] += 0.5
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1] + 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                     enimal_2[0], enimal_2[1] = enimal_2[0] + 1, enimal_2[1] + 1
#                 elif enimal_2[0] - 1 > 0 and enimal_2[1] - 1 > 0 and board[enimal_2[0] - 1][enimal_2[1] - 1] == 'f':
#                     board[enimal_2[0]][enimal_2[1]] += 1
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1] - 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                     enimal_2[0], enimal_2[1] = enimal_2[0] - 1, enimal_2[1] - 1
#                 elif enimal_2[0] - 1 > 0 and enimal_2[1] - 1 > 0 and board[enimal_2[0] - 1][enimal_2[1] - 1] == 'w':
#                     board[enimal_2[0]][enimal_2[1]] += 0.5
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1] - 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                     enimal_2[0], enimal_2[1] = enimal_2[0] - 1, enimal_2[1] - 1
#                 elif enimal_2[0] + 1 < len(board) and enimal_2[1] - 1 > 0 and board[enimal_2[0] + 1][
#                     enimal_2[1] - 1] == 'f':
#                     board[enimal_2[0]][enimal_2[1]] += 1
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1] - 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                     enimal_2[0], enimal_2[1] = enimal_2[0] + 1, enimal_2[1] - 1
#                 elif enimal_2[0] + 1 < len(board) and enimal_2[1] - 1 > 0 and board[enimal_2[0] + 1][
#                     enimal_2[1] - 1] == 'w':
#                     board[enimal_2[0]][enimal_2[1]] += 0.5
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1] - 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                     enimal_2[0], enimal_2[1] = enimal_2[0] + 1, enimal_2[1] - 1
#                 elif enimal_2[0] - 1 < len(board) and enimal_2[1] + 1 < len(board[enimal_2[0]]) and \
#                         board[enimal_2[0] - 1][enimal_2[1] + 1] == 'f':
#                     board[enimal_2[0]][enimal_2[1]] += 1
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1] + 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                     enimal_2[0], enimal_2[1] = enimal_2[0] - 1, enimal_2[1] + 1
#                 elif enimal_2[0] - 1 < len(board) and enimal_2[1] + 1 < len(board[enimal_2[0]]) and \
#                         board[enimal_2[0] - 1][enimal_2[1] + 1] == 'w':
#                     board[enimal_2[0]][enimal_2[1]] += 0.5
#                     board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1] + 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                     enimal_2[0], enimal_2[1] = enimal_2[0] - 1, enimal_2[1] + 1
#                 else:
#                     if enimal_2[1] + 1 < len(board[enimal_2[0]]):
#                         board[enimal_2[0]][enimal_2[1]] -= 1
#                         board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] + 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                         enimal_2[1] += 1
#                         if board[enimal_2[0]][enimal_2[1]] <= 0:
#                             board[enimal_2[0]][enimal_2[1]] = 'd'
#                             count += 1
#                     else:
#                         board[enimal_2[0]][enimal_2[1]] -= 1
#                         board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] - 1] = 0, \
#                                                                                                board[enimal_2[0]][
#                                                                                                    enimal_2[1]]
#                         enimal_2 -= 1
#                         if board[enimal_2[0]][enimal_2[1]] <= 0:
#                             board[enimal_2[0]][enimal_2[1]] = 'd'
#                             count += 1
#     return board


# 2 Ruben
def get_count_of_rectangles(dict_of_points):
    my_set = set()
    k = [el for el in dict_of_points.keys()]
    list_combinations = []
    for i in range(len(k)):
        string = k[i]
        for j in range(len(k)):
            if k[j] not in string:
                string = k[j] + k[i]
                for x in range(len(k)):
                    if k[x] not in string:
                        string = k[j] + k[i] + k[x]
                        for y in range(len(k)):
                            if k[y] not in string:
                                list_combinations.append(tuple(string + k[y]))

    for el in list_combinations:
        c_1 = dict_of_points[el[0]]
        c_2 = dict_of_points[el[1]]
        c_3 = dict_of_points[el[2]]
        c_4 = dict_of_points[el[3]]
        if c_1[0] == c_2[0] and c_2[1] == c_3[1] and c_3[0] == c_4[0] and c_1[1] == c_4[1]:
            my_set.add(''.join(sorted(list(el))))
    return my_set


print(get_count_of_rectangles({'A': (0, 0), 'B': (0, 4), 'C': (2, 0), 'D': (2, 4), 'E': (0, -4), 'F': (2, -4)}))