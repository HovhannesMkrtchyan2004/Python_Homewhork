# Ruben 1
# def rotateImage(a):
#     rotate_90 = []
#     for j in range(len(a)):
#         append_list = []
#         for i in range(len(a[j]) - 1, -1, -1):
#             append_list.append(a[i][j])
#         rotate_90.append(append_list)
#     return rotate_90
#
#
# a = [[10, 9, 6, 3, 7],
#      [6, 10, 2, 9, 7],
#      [7, 6, 3, 8, 2],
#      [8, 9, 7, 9, 9],
#      [6, 8, 6, 8, 2]]
# for el in rotateImage(a):
#     print(*el)

# Ruben 2
# def digitsProduct(product):
#     if product == 0:
#         return 10
#     number = ''
#     i = 9
#     while i >= 2 and product != 1:
#         if product % i == 0:
#             product /= i
#             number += str(i)
#             i = 9
#         else:
#             i -= 1
#     if product == 1:
#         return int(''.join(reversed(list(number))))
#     else:
#         return -1
#
#
# print(digitsProduct(19))

#Narek 1


