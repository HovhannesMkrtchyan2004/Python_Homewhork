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


# Ruben 1
def financialCrisis(roadRegister):
    ret_val = []
    for i in range(len(roadRegister)):
        pop_list = roadRegister.pop(i)
        append_list = []
        for j in range(len(roadRegister)):
            val = roadRegister[j].pop(i)
            append_list.append(roadRegister[j].copy())
            roadRegister[j].insert(i, val)
        ret_val.append(append_list)
        roadRegister.insert(i, pop_list)

    return ret_val


# Ruben 2
def namingRoads(roads):
    names = dict()
    for i in range(len(roads)):
        names[roads[i][-1]] = set(roads[i][:-1])
    for i in range(1, len(names)):
        if len(names[i - 1].union(names[i])) <= 3:
            return False
    return True
