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
# def answer_queries(k, *query_counts):
#     count = 1
#     query_counts = list(query_counts)
#     for i in range(len(query_counts)):
#         if query_counts[i] > k:
#             if i + 1 < len(query_counts):
#                 query_counts[i+1] += query_counts[i] - k
#                 count += 1
#             else:
#                 num = query_counts[i]
#                 while num >= k:
#                     count +=1
#                     num -= k
#         elif query_counts[i] == k:
#             count+=1
#         else:
#             return count
#     return count
# print(answer_queries( 5, 3,3,3,3))

# Ruben 2
def non_decreasing_sequence(*nums):
    nums = list(nums)
    for i in range(2, len(nums)):
        if (abs(nums[i - 1]) - abs(nums[i]) > 0 < abs(nums[i - 2]) - abs(nums[i - 1]) and nums[i - 1] != 0) or \
                (nums[i - 1] == 0 and nums[i - 2] != 0 and nums[i] != 0 and nums.count(0) > 1):
            return False
    return True


def ds(*nums):
    if non_decreasing_sequence(*nums):
        nums = [abs(el) for el in nums]
        nums[0] = -nums[0]
        for i in range(1, len(nums) - 1):
            if -nums[i] >= nums[i - 1]:
                nums[i] = -nums[i]
        return non_decreasing_sequence(*nums), nums
    return non_decreasing_sequence(*nums)
