#1
# import copy
# def rotateImage(a):
#     new_a = copy.deepcopy(a)
#     t = 1
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             new_a[j][len(new_a)-t] = a[i][j]
#         t += 1
#     return new_a
#
#
# ex1 = [[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]]
# ex2 = [[10, 9, 6, 3, 7],
#        [6, 10, 2, 9, 7],
#        [7, 6, 3, 8, 2],
#        [8, 9, 7, 9, 9],
#        [6, 8, 6, 8, 2]]
#
#
# print(rotateImage(ex2))


#2
def f(number):
    lst = []
    c = 2
    while number != 1:
        if number % c == 0:
            lst.append(c)
            number /= c
        else:
            c += 1
    return lst


def digitsProduct(product):
    if len(str(product)) == 1:
        return product
    number = ''
    lst = f(product)
    if len(lst) == 1:
        return -1
    number += str(lst[0])
    flag = True
    for i in range(2, len(lst)):
        if flag:
            if len(str(lst[i] * lst[i - 1])) == 1:
                number += str(lst[i] * lst[i - 1])
                flag = False
            else:
                number += str(lst[i])
                number += str(lst[i - 1])
        else:
            flag = True
    lst_ = list(map(int, list(number)))
    new_number = ''
    for el in sorted(lst_):
    	new_number += str(el)
    return int(new_number)
    
    
print(digitsProduct(450))
