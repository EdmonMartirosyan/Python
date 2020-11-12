#1
a = []
for _ in range(int(input())):
    a.append(input())
    a.append(float(input()))
b = [a[i] for i in range(1, len(a), 2)]
b.sort()
b.remove(min(b))
c = []
for i in b:
    if b[0] == i:
        c.append(i)
d = []
for el in c:
    d.append(a[a.index(el)-1])
    a.remove(a[a.index(el)-1])
    a.remove(el)
d.sort()
for el in d:
    print(el)

#2
# superString = input()
# subString = input()
# a = [superString.find(el) for el in subString]
# print(superString[:max(a)+1])

