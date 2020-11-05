# Narek 1
# def hexinak(hexinak, **kwargs):
#     hexinak_girq = kwargs[hexinak]
#     my_list = []
#     for i in range(0,len(hexinak_girq),2):
#         my_list.append([hexinak_girq[i + 1], hexinak_girq[i]])
#     for el in sorted(my_list):
#         print(*el)
#
#
# hexinak('h', h=['lutz', 2006, 'hovo', 2004, 'kikos', 10003, 'poxos', 8813])

# Narek 2
# def mult(list_):
#     print(list_)
#     flag = False
#     for el in list_:
#         if el > 0:
#             flag = True
#     if flag:
#         mult = list_.pop(list_.index(max(list_)))
#         max([-el for el in list_])
#         minus_1, minus_2 = sorted([-el for el in list_])[-1], sorted([-el for el in list_])[-2]
#         plus_1, plus_2 = sorted(list_)[-1], list_[-2]
#         if mult * plus_1 * plus_2 >= mult * minus_1 * minus_2:
#             return mult * plus_1 * plus_2
#         else:
#             return mult * minus_1 * minus_2
#     else:
#         return list_.pop(list_.index(max(list_))) * list_.pop(list_.index(max(list_))) * list_.pop(
#             list_.index(max(list_)))
#
#
# print(mult([-3, -5, -2, 20,1,33,-500]))
