n = input()
a = []
d = {}
while n != "End":
    a.append(int(n))
    n = input()
for el in a:
    d[el] = a.count(el)
print(d)