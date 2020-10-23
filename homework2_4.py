#1
def f(a):
    b = 2
    c = b
    while b < max(a):
        if b in a:
            c += 1
            b = c
        else:
            b += c
    return c
print(f([5, 3, 6, 7, 9]))
