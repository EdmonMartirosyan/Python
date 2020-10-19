#1
def f(a):
    count = 0
    for i in range(1, len(a)):
        if a[i] <= a[i-1]:
            a[i] += 1
            count += 1
    return count
print(f([1, 1, 1]))

#2
# def f(a):
#     count = 0
#     for i in range(1, len(a)):
#         if a[i] <= a[i-1]:
#             count += 1
#             a[i], a[len(a)-1] = a[len(a)-1], a[i]
#     return count == 1
# print(f([1, 2, 1, 2]))
