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


