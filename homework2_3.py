#1
# def f(a):
#     count = 0
#     for i in range(1, len(a)):
#         while a[i] <= a[i-1]:
#             a[i] += 1
#             count += 1
#     return count
# print(f([1, 1, 1]))

#2
# def f(a):
#     count = 0
#     for i in range(1, len(a)):
#         if a[i] <= a[i-1]:
#             count += 1
#     return count == 1
# print(f([1, 3, 4, 2, 6]))
