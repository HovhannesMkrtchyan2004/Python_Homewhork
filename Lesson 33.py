# 1 Narek
# def get_tree_coord(list_1):
#     tree_coord = []
#     for i in range(len(list_1)):
#         if list_1[i] == -1:
#             tree_coord.append(i)
#     for i in range(len(list_1)):
#         if list_1[i] == -1:
#             list_1.append(list_1.pop(i))
#     return tree_coord, list_1
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
my_list = [[10, 'f', 'w'],
           [0, 'w', 0],
           [0, 'w', 10]]


def get_coord_enimals(board):
    flag = False
    enimal_1 = list()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not (enimal_1) and board[i][j] == 10:
                enimal_1 = [i, j]
            elif enimal_1 and board[i][j] == 10:
                enimal_2 = [i, j]
                flag = True
    if flag:
        return [enimal_1, enimal_2]
    else:
        return enimal_1


def game(board):
    if len(get_coord_enimals(board)) == 2:
        enimal_1, enimal_2 = get_coord_enimals(board)
        count = 0
        while count != 2:
            if (abs(enimal_1[0] - enimal_2[0]) == 1 or abs(enimal_1[1] - enimal_2[1]) == 1) and count == 0:
                if board[enimal_1[0]][enimal_1[1]] - board[enimal_2[0]][enimal_2[1]] == 0:
                    board[enimal_1[0]][enimal_1[1]], board[enimal_2[0]][enimal_2[1]] = 'd', 'd'
                    return board
                elif board[enimal_1[0]][enimal_1[1]] - board[enimal_2[0]][enimal_2[1]] < 0:
                    board[enimal_2[0]][enimal_2[1]] -= board[enimal_1[0]][enimal_1[1]]
                    board[enimal_1[0]][enimal_1[1]] = 'd'
                    count += 1
                elif board[enimal_1[0]][enimal_1[1]] - board[enimal_2[0]][enimal_2[1]] > 0:
                    board[enimal_1[0]][enimal_1[1]] -= board[enimal_2[0]][enimal_2[1]]
                    board[enimal_2[0]][enimal_2[1]] = 'd'
                    count += 1
            elif abs(enimal_1[0] - enimal_2[0]) > 1 or abs(enimal_1[1] - enimal_2[1]) > 1 or count == 1:
                if board[enimal_1[0]][enimal_1[1]] != 'd':
                    if enimal_1[1] + 1 < len(board[enimal_1[0]]) and board[enimal_1[0]][enimal_1[1] + 1] == 'f':
                        board[enimal_1[0]][enimal_1[1]] += 1
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] + 1] = 0, board[enimal_1[0]][
                            enimal_1[1]]
                        enimal_1[1] += 1
                    elif enimal_1[1] + 1 < len(board[enimal_1[0]]) and board[enimal_1[0]][enimal_1[1] + 1] == 'w':
                        board[enimal_1[0]][enimal_1[1]] += 0.5
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] + 1] = 0, board[enimal_1[0]][
                            enimal_1[1]]
                        enimal_1[1] += 1
                    elif enimal_1[1] - 1 > 0 and board[enimal_1[0]][enimal_1[1] - 1] == 'f':
                        board[enimal_1[0]][enimal_1[1]] += 1
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] - 1] = 0, board[enimal_1[0]][
                            enimal_1[1]]
                        enimal_1[1] -= 1
                    elif enimal_1[1] - 1 > 0 and board[enimal_1[0]][enimal_1[1] - 1] == 'w':
                        board[enimal_1[0]][enimal_1[1]] += 0.5
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] - 1] = 0, board[enimal_1[0]][
                            enimal_1[1]]
                        enimal_1[1] -= 1
                    elif enimal_1[0] + 1 < len(board) and board[enimal_1[0] + 1][enimal_1[1]] == 'f':
                        board[enimal_1[0]][enimal_1[1]] += 1
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1]] = 0, board[enimal_1[0]][
                            enimal_1[1]]
                        enimal_1[0] += 1
                    elif enimal_1[0] + 1 > len(board) and board[enimal_1[0] + 1][enimal_1[1]] == 'w':
                        board[enimal_1[0]][enimal_1[1]] += 0.5
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1]] = 0, board[enimal_1[0]][
                            enimal_1[1]]
                        enimal_1[0] += 1
                    elif enimal_1[0] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1]] == 'f':
                        board[enimal_1[0]][enimal_1[1]] += 1
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1]] = 0, board[enimal_1[0]][
                            enimal_1[1]]
                        enimal_1[0] -= 1
                    elif enimal_1[0] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1]] == 'w':
                        board[enimal_1[0]][enimal_1[1]] += 0.5
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1]] = 0, board[enimal_1[0]][
                            enimal_1[1]]
                        enimal_1[0] -= 1
                    elif enimal_1[0] + 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
                            board[enimal_1[0] + 1][enimal_1[1] + 1] == 'f':
                        board[enimal_1[0]][enimal_1[1]] += 1
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] + 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                        enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] + 1
                    elif enimal_1[0] + 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
                            board[enimal_1[0] + 1][enimal_1[1] + 1] == 'w':
                        board[enimal_1[0]][enimal_1[1]] += 0.5
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] + 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                        enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] + 1
                    elif enimal_1[0] - 1 > 0 and enimal_1[1] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1] - 1] == 'f':
                        board[enimal_1[0]][enimal_1[1]] += 1
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] - 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                        enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] - 1
                    elif enimal_1[0] - 1 > 0 and enimal_1[1] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1] - 1] == 'w':
                        board[enimal_1[0]][enimal_1[1]] += 0.5
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] - 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                        enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] - 1
                    elif enimal_1[0] + 1 < len(board) and enimal_1[1] - 1 > 0 and board[enimal_1[0] + 1][
                        enimal_1[1] - 1] == 'f':
                        board[enimal_1[0]][enimal_1[1]] += 1
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] - 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                        enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] + 1
                    elif enimal_1[0] + 1 < len(board) and enimal_1[1] - 1 > 0 and board[enimal_1[0] + 1][
                        enimal_1[1] - 1] == 'w':
                        board[enimal_1[0]][enimal_1[1]] += 0.5
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] - 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                        enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] - 1
                    elif enimal_1[0] - 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
                            board[enimal_1[0] - 1][enimal_1[1] + 1] == 'f':
                        board[enimal_1[0]][enimal_1[1]] += 1
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] + 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                        enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] + 1
                    elif enimal_1[0] - 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
                            board[enimal_1[0] - 1][enimal_1[1] + 1] == 'w':
                        board[enimal_1[0]][enimal_1[1]] += 0.5
                        board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] + 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                        enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] + 1
                    else:
                        if enimal_1[1] + 1 < len(board[enimal_1[0]]):
                            board[enimal_1[0]][enimal_1[1]] -= 1
                            board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] + 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                            enimal_1[1] += 1
                            if board[enimal_1[0]][enimal_1[1]] <= 0:
                                board[enimal_1[0]][enimal_1[1]] = 'd'
                                count += 1
                        else:
                            board[enimal_1[0]][enimal_1[1]] -= 1
                            board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] - 1] = 0, \
                                                                                                   board[enimal_1[0]][
                                                                                                       enimal_1[1]]
                            enimal_1[1] -= 1
                            if board[enimal_1[0]][enimal_1[1]] <= 0:
                                board[enimal_1[0]][enimal_1[1]] = 'd'
                                count += 1
                if board[enimal_2[0]][enimal_2[1]] != 'd':
                    if enimal_2[1] + 1 < len(board[enimal_2[0]]) and board[enimal_2[0]][enimal_2[1] + 1] == 'f':
                        board[enimal_2[0]][enimal_2[1]] += 1
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] + 1] = 0, board[enimal_2[0]][
                            enimal_2[1]]
                        enimal_2[1] += 1
                    elif enimal_2[1] + 1 < len(board[enimal_2[0]]) and board[enimal_2[0]][enimal_2[1] + 1] == 'w':
                        board[enimal_2[0]][enimal_2[1]] += 0.5
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] + 1] = 0, board[enimal_2[0]][
                            enimal_2[1]]
                        enimal_2[1] += 1
                    elif enimal_2[1] - 1 > 0 and board[enimal_2[0]][enimal_2[1] - 1] == 'f':
                        board[enimal_2[0]][enimal_2[1]] += 1
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] - 1] = 0, board[enimal_2[0]][
                            enimal_2[1]]
                        enimal_2[1] -= 1
                    elif enimal_2[1] - 1 > 0 and board[enimal_2[0]][enimal_2[1] - 1] == 'w':
                        board[enimal_2[0]][enimal_2[1]] += 0.5
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] - 1] = 0, board[enimal_2[0]][
                            enimal_2[1]]
                        enimal_2[1] -= 1
                    elif enimal_2[0] + 1 < len(board) and board[enimal_2[0] + 1][enimal_2[1]] == 'f':
                        board[enimal_2[0]][enimal_2[1]] += 1
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1]] = 0, board[enimal_2[0]][
                            enimal_2[1]]
                        enimal_2[0] += 1
                    elif enimal_2[0] + 1 > len(board) and board[enimal_2[0] + 1][enimal_2[1]] == 'w':
                        board[enimal_2[0]][enimal_2[1]] += 0.5
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1]] = 0, board[enimal_2[0]][
                            enimal_2[1]]
                        enimal_2[0] += 1
                    elif enimal_2[0] - 1 > 0 and board[enimal_2[0] - 1][enimal_2[1]] == 'f':
                        board[enimal_2[0]][enimal_2[1]] += 1
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1]] = 0, board[enimal_2[0]][
                            enimal_2[1]]
                        enimal_2[0] -= 1
                    elif enimal_2[0] - 1 > 0 and board[enimal_2[0] - 1][enimal_2[1]] == 'w':
                        board[enimal_2[0]][enimal_2[1]] += 0.5
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1]] = 0, board[enimal_2[0]][
                            enimal_2[1]]
                        enimal_2[0] -= 1
                    elif enimal_2[0] + 1 < len(board) and enimal_2[1] + 1 < len(board[enimal_2[0]]) and \
                            board[enimal_2[0] + 1][enimal_2[1] + 1] == 'f':
                        board[enimal_2[0]][enimal_2[1]] += 1
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1] + 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                        enimal_2[0], enimal_2[1] = enimal_2[0] + 1, enimal_2[1] + 1
                    elif enimal_2[0] + 1 < len(board) and enimal_2[1] + 1 < len(board[enimal_2[0]]) and \
                            board[enimal_2[0] + 1][enimal_2[1] + 1] == 'w':
                        board[enimal_2[0]][enimal_2[1]] += 0.5
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1] + 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                        enimal_2[0], enimal_2[1] = enimal_2[0] + 1, enimal_2[1] + 1
                    elif enimal_2[0] - 1 > 0 and enimal_2[1] - 1 > 0 and board[enimal_2[0] - 1][enimal_2[1] - 1] == 'f':
                        board[enimal_2[0]][enimal_2[1]] += 1
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1] - 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                        enimal_2[0], enimal_2[1] = enimal_2[0] - 1, enimal_2[1] - 1
                    elif enimal_2[0] - 1 > 0 and enimal_2[1] - 1 > 0 and board[enimal_2[0] - 1][enimal_2[1] - 1] == 'w':
                        board[enimal_2[0]][enimal_2[1]] += 0.5
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1] - 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                        enimal_2[0], enimal_2[1] = enimal_2[0] - 1, enimal_2[1] - 1
                    elif enimal_2[0] + 1 < len(board) and enimal_2[1] - 1 > 0 and board[enimal_2[0] + 1][
                        enimal_2[1] - 1] == 'f':
                        board[enimal_2[0]][enimal_2[1]] += 1
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1] - 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                        enimal_2[0], enimal_2[1] = enimal_2[0] + 1, enimal_2[1] - 1
                    elif enimal_2[0] + 1 < len(board) and enimal_2[1] - 1 > 0 and board[enimal_2[0] + 1][
                        enimal_2[1] - 1] == 'w':
                        board[enimal_2[0]][enimal_2[1]] += 0.5
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] + 1][enimal_2[1] - 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                        enimal_2[0], enimal_2[1] = enimal_2[0] + 1, enimal_2[1] - 1
                    elif enimal_2[0] - 1 < len(board) and enimal_2[1] + 1 < len(board[enimal_2[0]]) and \
                            board[enimal_2[0] - 1][enimal_2[1] + 1] == 'f':
                        board[enimal_2[0]][enimal_2[1]] += 1
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1] + 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                        enimal_2[0], enimal_2[1] = enimal_2[0] - 1, enimal_2[1] + 1
                    elif enimal_2[0] - 1 < len(board) and enimal_2[1] + 1 < len(board[enimal_2[0]]) and \
                            board[enimal_2[0] - 1][enimal_2[1] + 1] == 'w':
                        board[enimal_2[0]][enimal_2[1]] += 0.5
                        board[enimal_2[0]][enimal_2[1]], board[enimal_2[0] - 1][enimal_2[1] + 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                        enimal_2[0], enimal_2[1] = enimal_2[0] - 1, enimal_2[1] + 1
                    else:
                        if enimal_2[1] + 1 < len(board[enimal_2[0]]):
                            board[enimal_2[0]][enimal_2[1]] -= 1
                            board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] + 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                            enimal_2[1] += 1
                            if board[enimal_2[0]][enimal_2[1]] <= 0:
                                board[enimal_2[0]][enimal_2[1]] = 'd'
                                count += 1
                        else:
                            board[enimal_2[0]][enimal_2[1]] -= 1
                            board[enimal_2[0]][enimal_2[1]], board[enimal_2[0]][enimal_2[1] - 1] = 0, \
                                                                                                   board[enimal_2[0]][
                                                                                                       enimal_2[1]]
                            enimal_2 -= 1
                            if board[enimal_2[0]][enimal_2[1]] <= 0:
                                board[enimal_2[0]][enimal_2[1]] = 'd'
                                count += 1



    else:
        enimal_1 = get_coord_enimals(board)
        count = 0
        while count != 1:
            if enimal_1[1] + 1 < len(board[enimal_1[0]]) and board[enimal_1[0]][enimal_1[1] + 1] == 'f':
                board[enimal_1[0]][enimal_1[1]] += 1
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] + 1] = 0, board[enimal_1[0]][
                    enimal_1[1]]
                enimal_1[1] += 1
            elif enimal_1[1] + 1 < len(board[enimal_1[0]]) and board[enimal_1[0]][enimal_1[1] + 1] == 'w':
                board[enimal_1[0]][enimal_1[1]] += 0.5
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] + 1] = 0, board[enimal_1[0]][
                    enimal_1[1]]
                enimal_1[1] += 1
            elif enimal_1[1] - 1 > 0 and board[enimal_1[0]][enimal_1[1] - 1] == 'f':
                board[enimal_1[0]][enimal_1[1]] += 1
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] - 1] = 0, board[enimal_1[0]][
                    enimal_1[1]]
                enimal_1[1] -= 1
            elif enimal_1[1] - 1 > 0 and board[enimal_1[0]][enimal_1[1] - 1] == 'w':
                board[enimal_1[0]][enimal_1[1]] += 0.5
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] - 1] = 0, board[enimal_1[0]][
                    enimal_1[1]]
                enimal_1[1] -= 1
            elif enimal_1[0] + 1 < len(board) and board[enimal_1[0] + 1][enimal_1[1]] == 'f':
                board[enimal_1[0]][enimal_1[1]] += 1
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1]] = 0, board[enimal_1[0]][
                    enimal_1[1]]
                enimal_1[0] += 1
            elif enimal_1[0] + 1 > len(board) and board[enimal_1[0] + 1][enimal_1[1]] == 'w':
                board[enimal_1[0]][enimal_1[1]] += 0.5
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1]] = 0, board[enimal_1[0]][
                    enimal_1[1]]
                enimal_1[0] += 1
            elif enimal_1[0] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1]] == 'f':
                board[enimal_1[0]][enimal_1[1]] += 1
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1]] = 0, board[enimal_1[0]][
                    enimal_1[1]]
                enimal_1[0] -= 1
            elif enimal_1[0] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1]] == 'w':
                board[enimal_1[0]][enimal_1[1]] += 0.5
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1]] = 0, board[enimal_1[0]][
                    enimal_1[1]]
                enimal_1[0] -= 1
            elif enimal_1[0] + 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
                    board[enimal_1[0] + 1][enimal_1[1] + 1] == 'f':
                board[enimal_1[0]][enimal_1[1]] += 1
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] + 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] + 1
            elif enimal_1[0] + 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
                    board[enimal_1[0] + 1][enimal_1[1] + 1] == 'w':
                board[enimal_1[0]][enimal_1[1]] += 0.5
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] + 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] + 1
            elif enimal_1[0] - 1 > 0 and enimal_1[1] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1] - 1] == 'f':
                board[enimal_1[0]][enimal_1[1]] += 1
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] - 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] - 1
            elif enimal_1[0] - 1 > 0 and enimal_1[1] - 1 > 0 and board[enimal_1[0] - 1][enimal_1[1] - 1] == 'w':
                board[enimal_1[0]][enimal_1[1]] += 0.5
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] - 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] - 1
            elif enimal_1[0] + 1 < len(board) and enimal_1[1] - 1 > 0 and board[enimal_1[0] + 1][
                enimal_1[1] - 1] == 'f':
                board[enimal_1[0]][enimal_1[1]] += 1
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] - 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] + 1
            elif enimal_1[0] + 1 < len(board) and enimal_1[1] - 1 > 0 and board[enimal_1[0] + 1][
                enimal_1[1] - 1] == 'w':
                board[enimal_1[0]][enimal_1[1]] += 0.5
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] + 1][enimal_1[1] - 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                enimal_1[0], enimal_1[1] = enimal_1[0] + 1, enimal_1[1] - 1
            elif enimal_1[0] - 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
                    board[enimal_1[0] - 1][enimal_1[1] + 1] == 'f':
                board[enimal_1[0]][enimal_1[1]] += 1
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] + 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] + 1
            elif enimal_1[0] - 1 < len(board) and enimal_1[1] + 1 < len(board[enimal_1[0]]) and \
                    board[enimal_1[0] - 1][enimal_1[1] + 1] == 'w':
                board[enimal_1[0]][enimal_1[1]] += 0.5
                board[enimal_1[0]][enimal_1[1]], board[enimal_1[0] - 1][enimal_1[1] + 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                enimal_1[0], enimal_1[1] = enimal_1[0] - 1, enimal_1[1] + 1
            else:
                if enimal_1[1] + 1 < len(board[enimal_1[0]]):
                    board[enimal_1[0]][enimal_1[1]] -= 1
                    board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] + 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                    enimal_1[1] += 1
                    if board[enimal_1[0]][enimal_1[1]] <= 0:
                        count += 1
                else:
                    board[enimal_1[0]][enimal_1[1]] -= 1
                    board[enimal_1[0]][enimal_1[1]], board[enimal_1[0]][enimal_1[1] - 1] = 0, \
                                                                                           board[enimal_1[0]][
                                                                                               enimal_1[1]]
                    enimal_1 -= 1
                    if board[enimal_1[0]][enimal_1[1]] <= 0:
                        board[enimal_1[0]][enimal_1[1]] = 'd'
                        count += 1
    return board


for el in game(my_list):
    print(*el)
# 1 Ruben
# def swap_list_elements(list_1):
#     for i in range(len(list_1)):
#         if list_1[i] % 2 and i % 2 == 0:
#             j = i
#             while j < len(list_1):
#                 if list_1[j] % 2 == 0 and j % 2:
#                     list_1[i], list_1[j] = list_1[j], list_1[i]
#                     break
#                 j += 1
#         elif list_1[i] % 2 == 0 and i % 2:
#             j = i
#             while j < len(list_1):
#                 if list_1[j] % 2 and j % 2 == 0:
#                     list_1[i], list_1[j] = list_1[j], list_1[i]
#                 j += 1
#     return list_1

# 2 Ruben
# def get_count_of_rectangles(dict_of_points):
#     for el in dict_of_points.key():
