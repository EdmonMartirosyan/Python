#1
import copy
def rotateImage(a):
    new_a = copy.deepcopy(a)
    t = 1
    for i in range(len(a)):
        for j in range(len(a[i])):
            new_a[j][len(new_a)-t] = a[i][j]
        t += 1
    return new_a


ex1 = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
ex2 = [[10, 9, 6, 3, 7],
       [6, 10, 2, 9, 7],
       [7, 6, 3, 8, 2],
       [8, 9, 7, 9, 9],
       [6, 8, 6, 8, 2]]


print(rotateImage(ex2))
