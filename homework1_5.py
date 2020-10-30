#1
def possible_turns(cell):
    letters = "ABCDEFGH"
    list_ = []
    a = letters.find(cell[0])+1
    for i in range(1, 9):
        for j in letters:
            b = letters.find(j)+1
            if abs(int(cell[1]) - i) == 1 and abs(a-b) == 2 or abs(int(cell[1]) - i) == 2 and abs(a-b) == 1:
                list_.append(f"{j}{i}")
    return list_


print(possible_turns("E4"))
