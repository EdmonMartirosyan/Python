#1
def chess(a, b):
    letters = "ABCDEFGH"
    return abs(int(a[1]) - int(b[1])) % 2 == abs(letters.find(a[0])+1 - letters.find(b[0])+1) % 2


print(chess("A1", "B5"))

