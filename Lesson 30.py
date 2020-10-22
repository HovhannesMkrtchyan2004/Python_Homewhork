# Ruben 1
# matrix = [[True, False, False],
#           [False, True, False],
#           [True, False, True]]
#
#
# def minesweeper(m):
#     true = [[i, j] for i in range(3) for j in range(3) if m[i][j]]
#     m = [[0 for j in range(3)] for i in range(3)]
#     for i in range(len(true)):
#         x, y = true[i]
#         for j in range(3):
#             for k in range(3):
#                 if abs(j - x) == 1 and abs(k - y) <= 1 or abs(j - x) == 0 and abs(k - y) == 1:
#                     m[j][k] += 1
#     return m
#
#
# print(minesweeper(matrix))


# 2 Ruben
# string = input()
# vow = [string[i:j+1] for i in range(len(string)) if string[i].lower() in 'aeuio' for j in range(i+1, len(string))]
# con = [string[i:j+1] for i in range(len(string)) if string[i].lower() not in 'aeuio' for j in range(i+1,len(string))]
#
# print({el: string.count(el) for el in vow})
# print({el: string.count(el) for el in con})

# Narek 1
# x = [5, 3, 6, 7, 9]
# i = 2
# qayl = 0
# while i < max(x) + 1:
#     if qayl not in x:
#         qayl += i
#         if qayl > max(x):
#             print(i)
#             break
#         continue
#     qayl = 0
#     i += 1

# Narek 2
x = input().split('=')
y = list(x[0])
for i in range(len(x[0])):
    if x[0][i] == '+':
        x[1] += '-'
        j = i + 1
        while j < len(x[0]) and x[0][j].isdigit():
            x[1] += x[0][j]
            j += 1
    elif x[0][i] == '-':
        x[1] += '+'
        j = i + 1
        while j < len(x[0]) and x[0][j].isdigit():
            x[1] += x[0][j]
            j += 1

count = 0
for i in range(len(x[1]) - 1, -1, -1):
    if x[1][i] == '+':
        j = i + 1
        z = ''
        while j < len(x[1]) and x[1][j].isdigit():
            z += x[1][j]
            j += 1
        if len(z)>0:
            count += int(z)
    elif x[1][i] == '-':
        j = i + 1
        z = ''
        while j < len(x[1]) and x[1][j].isdigit():
            z += x[1][j]
            j += 1
        if len(z)>0:
            count -= int(z)
    elif i == 0 and x[1][i].isdigit():
        j = i
        z = ''
        while j < len(x[1]) and x[1][j].isdigit():
            z += x[1][j]
            j += 1
        count += + int(z)
count_x = 0
for i in range(len(x[0])):
    if x[0][i] == 'x':
        if i == 0:
            count_x += 1
        elif x[0][i-1].isdigit():
            j = i - 1
            z = ''
            while j >= 0 and x[1][j].isdigit():
                z += x[0][j]
                j -= 1
            if len(z):
                count_x += int(z)
        else:
            count_x += 1

print('x =', int(count/count_x))
