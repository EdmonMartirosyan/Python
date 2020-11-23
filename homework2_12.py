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
    if lst[0] == len(lucky_number.list_1):
        return lst[0]
    else:
        new_list = lst[lst[0]-len(lucky_number.list_1):]
        if len(new_list) == 0:
            return -1
        lucky_number.list_1 += lst[:lst[0]-len(lucky_number.list_1)]
        return lucky_number(new_list)


lucky_number.list_1 = []
print(lucky_number([1, 2, 2, 5, 7]))
