# 1 Narek
# a = [1, 5, 1]
# def func(a):
#     count = 0
#     for i in range(1, len(a)):
#         while a[i - 1] >= a[i]:
#             a[i] += 1
#             count += 1
#     return count
#
#
# print(func(a))


# 2 Narek
# a = [1,1,1,3,2]
#
#
# def func(a):
#     count = 0
#     for i in range(len(a) - 1):
#         x = a.pop(i)
#         if x in a:
#             count += 1
#         if count == 2:
#             return False
#         if a == sorted(a):
#             return True
#         else:
#             a.insert(i, x)
#     return False
#
#
# print(func(a))


# 3 Ruben
# n = int(input())
# my_list = []
# name = []
# for _ in range(n):
#     my_list.append([input(), float(input())])
#
# tver = [el[1] for el in my_list]
# minimum = min(tver)
# while minimum in tver:
#     tver.remove(minimum)
#
# for i in range(n):
#     if my_list[i][1] == min(tver):
#         name.append(my_list[i][0])
#
# for el in sorted(name):
#     print(el)


# 4 Ruben
super_string = input()
sub_string = list(input())
my_list = []
sub_string_tar = []
for i in range(len(super_string)):
    if super_string[i] in sub_string:
        sub_string_tar.append(sub_string.pop(sub_string.index(super_string[i])))
        j = i
        while j < len(super_string) and len(sub_string) != 0:
            if super_string[j] in sub_string:
                sub_string_tar.append(sub_string.pop(sub_string.index(super_string[j])))
            j += 1
        if len(sub_string) == 0:
            my_list.append(super_string[i:j])
    sub_string, sub_string_tar = sub_string_tar, sub_string

for i in range(len(my_list)):
    y = 0
    if len(my_list[y]) > len(my_list[i]):
        y = i
print(my_list[y])



