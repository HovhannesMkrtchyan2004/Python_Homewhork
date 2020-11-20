# Ruben 1 Es u Arsen miasin enq lucel
# def newRoadSystem(roadRegister):
#     roadRegister2 = list(zip(*roadRegister))
#     for i in range(len(roadRegister)):
#         if roadRegister[i].count(True) != roadRegister2[i].count(True):
#             return False
#     return True
#
#
# Ruben 2 Es u Arseny miasin enq luscel
# def find_neighbour(num, roads):
#     my_list = []
#     for j in range(len(roads)):
#         if num in roads[j]:
#             if roads[j][0] == num:
#                 my_list.append(roads[j][1])
#             else:
#                 my_list.append(roads[j][0])
#     return my_list
#
#
# def efficientRoadNetwork(n, roads):
#     if n == 1:
#         return True
#     for i in range(n):
#         neighbours = tuple(find_neighbour(i, roads))
#         my_set = [*neighbours]
#         for el in neighbours:
#             my_set.extend(find_neighbour(el, roads))
#         if len(set(my_set)) != n:
#             return False
#     return True

# Narek 1
# def num(number):
#     num_list = []
#     count = 1
#     for i in range(1, number+1):
#         num_list.append(i)
#         if count == len(num_list):
#             print(*num_list)
#             num_list = []
#             count +=1
#     print(*num_list)
#
#
# num(11)

# Narek 2
# def successful_number(list_):
#     i = 0
#     j = len(list_) - 1
#     while list_[i:j + 1]:
#         k = (i + j) // 2
#         if list_[k] == k:
#             return k
#         elif list_[k] > k:
#             j = k - 1
#         else:
#             i = k + 1
#     return -1
#
#
# print(successful_number([-1, 0, 1, 2, 3, 7, 8]))
