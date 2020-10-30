#1
def f(a):
    b = 2
    c = b
    while b <= max(a):
        if b in a:
            c += 1
            b = c
        else:
            b += c
    return c
<<<<<<< HEAD
print(f([2, 3]))
=======
print(f([5, 3, 6, 7, 9]))

>>>>>>> 510789ea0abdd7016718386b9551a3b1dae43c02
