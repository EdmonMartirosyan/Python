word = input()
c = 0
if len(word) % 2 == 0:
    for el in word:
        if word.count(el) % 2 != 0:
            print(False)
            break
    else:
        print(True)
else:
    for el in word:
        if word.count(el) % 2 != 0:
            if c == 0:
                c += 1
            else:
                print(False)
                break
    else:
        print(True)





