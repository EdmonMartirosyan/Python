#1
# def number_of_digits(n):
#     a = 10
#     count = 1
#     while a <= n:
#         a *= 10
#         count +=1
#     return count
# 
# 
# print(number_of_digits(432))

#2
def sum_numbers(lst, n):
    set_ = set()
    for i in range(len(lst)):
        if n - lst[i] in lst:
            set_.add((lst[i], n - lst[i]))
    return


print(sum_numbers([5, 2, 2, 5, 3],8))
