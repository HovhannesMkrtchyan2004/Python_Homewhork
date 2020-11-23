# Narek 1
def find_number_in_nested_list(list_, num):
    for k in range(len(list_)):
        i = 0
        j = len(list_[k]) - 1
        while list_[k][i:j + 1]:
            z = (i + j) // 2
            if list_[k][z] == num:
                return k, z
            elif list_[k][z] > num:
                j = z - 1
            else:
                i = z + 1
    return -1


print(find_number_in_nested_list([[10, 20, 30, 40],
                                  [15, 25, 35, 45],
                                  [27, 29, 37, 48],
                                  [32, 33, 39, 50]], 29))


# Narek 2
def strings_equal(str1, str2):
    print(sorted(str1) == sorted(str2))


strings_equal('abvdj', 'vjdab')
