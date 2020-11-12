#1
# def answer_queries(k, *query_counts):
#     count = 0
#     number = 0
#     for i in range(len(query_counts)):
#         if query_counts[i] + count >= k:
#             count = query_counts[i] + count - k
#             number += 1
#         else:
#             return number+1
#     if count > 0:
#         number += count // k
#     return number+1
#
<<<<<<< HEAD
# print(answer_queries(5, 5))


#2
def non_decreasing_sequence(*nums):
    nums_list = list(nums)
    set_ = set()
    for i in range(len(nums_list)):
        if nums_list != sorted(nums_list):
            if i > 0:
                if i < len(nums_list)-1:
                    if abs(nums_list[i]) > abs(nums_list[i-1]) and abs(nums_list[i]) < abs(nums_list[i+1]):
                        continue
                elif nums_list[i] < nums_list[i-1]:
                    nums_list[i] = -nums_list[i]
            elif nums_list[i] > abs(nums_list[i+1]):
                nums_list[i] = -nums_list[i]
        else:
            set_.add(tuple(nums_list))
    if set_:
        print("Yes", list(*set_), sep="\n")
    else:
        print("No")


non_decreasing_sequence(2, 3, -5, 7)
=======
#
# print(answer_queries(5, 10, 5, 5, 3, 2, 1))

#2
def non_decreasing_sequence(*nums):
    nums_list = list(nums)
    set_ = set()
    for i in range(len(nums_list)):
        if nums_list != sorted(nums_list):
            nums_list[i] = -nums_list[i]
        else:
            set_.add(tuple(nums_list))
    if set_:
        print("Yes", list(*set_), sep="\n")
    else:
        print("No")
>>>>>>> 384f16298b88545275849deba9ff78d8c70b6791


non_decreasing_sequence(1, 1, 0)
