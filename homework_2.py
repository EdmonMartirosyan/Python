word = input()
c = 0
for el in word:
    if word.count(el) % 2 != 0:
        if len(word) % 2 == 1:
            if c == 0:
                c += 1
                continue
        print(False)
        break
else:
    print(True)





