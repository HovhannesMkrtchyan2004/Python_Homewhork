# 1 Narek
# def Tic_Tac_Toe(tictactoe):
#     x = 'x'
#     o = 'o'
#     for i in range(len(tictactoe)):
#         j = 0
#         while j < len(tictactoe[0]) and tictactoe[i][j] == x:
#             j += 1
#         if j == len(tictactoe[0]):
#             return x
#     for k in range(len(tictactoe)):
#         j = 0
#         while j < len(tictactoe) and tictactoe[j][k] == x:
#             j += 1
#         if j == len(tictactoe):
#             return x
#     k = 0
#     j = 0
#     while j < len(tictactoe) and tictactoe[k][j] == x:
#         j, k = j + 1, k + 1
#     if j == len(tictactoe):
#         return x
#     # o-i hamar - nuyny
#     for i in range(len(tictactoe)):
#         j = 0
#         while j < len(tictactoe[0]) and tictactoe[i][j] == o:
#             j += 1
#         if j == len(tictactoe[0]):
#             return o
#     for k in range(len(tictactoe)):
#         j = 0
#         while j < len(tictactoe) and tictactoe[j][k] == o:
#             j += 1
#         if j == len(tictactoe):
#             return o
#     k = 0
#     j = 0
#     while j < len(tictactoe) and tictactoe[k][j] == o:
#         j, k = j + 1, k + 1
#     if j == len(tictactoe):
#         return o
#
#     for i in range(len(tictactoe)):
#         if 'Empty' in tictactoe[i]:
#             count_x = 0
#             count_o = 0
#             for j in range(len(tictactoe)):
#                 count_o += tictactoe[j].count(o)
#                 count_x += tictactoe[j].count(x)
#             if count_x > count_o:
#                 return o
#             else:
#                 return x
#     return -1
#
#
# l = [['x', 'o', 'x'],
#      ['x', 'x', 'o'],
#      ['o', 'x', 'o']]
# print(Tic_Tac_Toe(l))

# 2 Narek
# def digital_progress(progress):
#     i = 3
#     progress_plus = progress[1]
#     j = 2
#     while i <= progress[2] and j < len(progress):
#         if progress_plus + i <= progress[j]:
#             progress_plus += i
#         elif progress[j] - progress_plus == 0:
#             j += 1
#         else:
#             progress_plus = progress[1]
#             i += 1
#             j = 2
#     print(i <= progress[2])
#
#
# digital_progress([1,5,23,32])

# 1 Ruben
# def groups(group):
#     group = group.split(', ')
#     child_count = []
#     child_names = []
#     for el in group:
#         for elem in el:
#             if elem.isdigit():
#                 child_count.append(int(elem))
#     for i in range(len(group)):
#         child_names.append(input().split(', '))
#     dict_group = dict()
#     for el in child_names:
#         dict_group[group[child_count.index(len(el))].split(':')[0]] = el
#
#     output_child = input().split(', ')
#     count = []
#     for i in range(len(output_child)):
#         count_append = 0
#         for el in child_names:
#             if output_child[i] in el:
#                 count_append += 1
#         count.append([count_append, output_child[i]])
#     output_name = sorted([el[1] for el in count if el[0] == min(count)[0]])[0]
#     group_names = []
#     for key, value in dict_group.items():
#         if output_name in value:
#             group_names.append(key)
#     print(output_name + ':', ' '.join(group_names))
#
#
# groups(input())

# 2 Ruben
name = []
cost = []


def add_item(itemName, itemCost):
    name.append(itemName)
    cost.append(itemCost)


check_count = 0


def print_receipt():
    global name, cost
    if name:
        global check_count
        check_count += 1
        print('Check ', check_count, '. Number of items: ', len(name))
        for i in range(len(name)):
            print(name[i], ' - ', cost[i])
        print('Total: ', sum(cost))
        print('-----')
        name = []
        cost = []



