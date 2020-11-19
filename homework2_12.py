#1
# def print_numbers(n):
#     a = 1
#     b = 1
#     for i in range(1, n+1):
#         if a > b:
#             print()
#             b += 1
#             a = 1
#         if a <= b:
#             print(i, end=" ")
#             a += 1
#
#
# print_numbers(9)


#2
def lucky_number(lst):
    for i in range(len(lst)):
        if i == lst[i]:
            return lst[i]
    else:
        return -1


print(lucky_number([5, 3, 1, 2, 4, 10]))

