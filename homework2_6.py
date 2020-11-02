#1
def f(a):
    b = []
    c = []
    for i in range(len(a)):
        if a[i] != -1:
            b.append(a[i])
        else:
            c.append(i)
    b.sort()
    for j in range(len(c)):
        b.insert(c[j], -1)
    return b
print(f([2, -1, 1, 5, 4, -1, 3]))

