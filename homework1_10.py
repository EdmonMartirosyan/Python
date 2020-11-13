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
    lst = [j for i in range(n+1) for j in str(i)]
    return lst.count("2")


print(func(22))
