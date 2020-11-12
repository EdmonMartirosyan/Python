#1
# import math
#
#
# def absolute_difference(list_):
#     diff = -math.inf
#     for i in range(1, len(list_)):
#         if abs(list_[i] - list_[i-1]) > diff:
#             diff = abs(list_[i] - list_[i-1])
#     return diff
#
#
# print(absolute_difference([5, 9, 2, 12, 5, 8]))

#2
def func(n):
    count = 0
    for i in range(n+1):
        if "2" in str(i):
            count += str(i).count("2")
    return count


print(func(22))

