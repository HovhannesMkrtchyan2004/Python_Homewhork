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
#     list_.sort()
#     mult = list_.pop()
#     if mult * list_[-1] * list_[-2] >= mult * list_[0] * list_[1]:
#         return mult * list_[-1] * list_[-2]
#     else:
#         return mult * list_[0] * list_[1]
#
#
# print(mult([9,5,8,5,20,1,2,-3,-2,-1,0]))


# Ruben 1
# def find_small_number(k,query_counts):
#     for i in range(len(query_counts)):
#         if query_counts[i]<k:
#             return query_counts[i]
#     return False
#
#
# def answer_queries(k, *query_counts):
#     query_counts = list(query_counts)
#     count = 1
#     if find_small_number(k,query_counts):
#         summ = sum(query_counts[:query_counts.index(find_small_number(k,query_counts))+1])
#     else:
#         summ = sum(query_counts)
#
#     while summ >= k:
#         summ -= k
#         count += 1
#     return count
#
#
# print(answer_queries(5, 10, 5, 5, 3, 2, 1))

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

# print(non_decreasing_sequence( -2, -3, -1 ))
