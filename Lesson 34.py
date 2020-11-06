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

# Ruben 1
# def answer_queries(k, *query_counts):
#     count = 1
#     summ = sum(query_counts)
#     while summ >= k:
#         summ -= k
#         count += 1
#     return  count
#
#
# print(answer_queries(1, 100))

# Ruben 2
def non_decreasing_sequence(*nums):
    # flag = False
    nums = list(nums)
    for i in range(2, len(nums)):
        if nums[i - 2] <= nums[i - 1] <= nums[i] and nums == sorted(nums):
            return True, nums
        if nums[i - 2] <= nums[i - 1] > nums[i]:
            if nums[i - 2] <= nums[i - 1] <= -nums[i] or -nums[i - 2] <= -nums[i - 1] <= nums[i]:
                nums[i] = -nums[i]
                if nums == sorted(nums):
                    return True, nums
                elif not nums[i - 2] <= nums[i - 1] <= nums[i]:
                    nums[i] = -nums[i]
                nums[i - 1] = -nums[i - 1]
                if nums == sorted(nums):
                    return True, nums
                elif not nums[i - 1] <= nums[i]:
                    nums[i - 1] = -nums[i - 1]
                nums[i - 2] = -nums[i - 2]
                if nums == sorted(nums):
                    return True, nums
                elif not nums[i - 2] <= nums[i - 1]:
                    nums[i - 2] = -nums[i - 2]
        if nums[i - 2] > nums[i - 1] > nums[i]:
            if -nums[i - 2] <= -nums[i - 1] <= -nums[i]:
                nums[i - 2], nums[i - 1], nums[i] = -nums[i - 2], -nums[i - 1], -nums[i]
                if nums == sorted(nums):
                    return True, nums
                elif not nums[i - 2] <= nums[i - 1] <= nums[i]:
                    nums[i - 2], nums[i - 1], nums[i] = -nums[i - 2], -nums[i - 1], -nums[i]
        if nums[i - 2] > nums[i - 1] < nums[i]:
            if -nums[i - 2] <= nums[i - 1] <= nums[i] or nums[i - 2] <= -nums[i - 1] <= nums[i]:
                nums[i - 2] = -nums[i - 2]
                if nums == sorted(nums):
                    return True, nums
                elif not nums[i - 2] <= nums[i - 1] <= nums[i]:
                    nums[i - 2] = -nums[i - 2]
                nums[i - 1] = -nums[i - 1]
                if nums == sorted(nums):
                    return True, nums
                elif not nums[i - 2] <= nums[i - 1] <= nums[i]:
                    nums[i - 1] = -nums[i - 1]

    return False


print(non_decreasing_sequence(  1, -1, -2, 3, 6,-7))
