#1
def number_of_digits(n):
    a = 10
    count = 1
    while a <= n:
        a *= 10
        count +=1
    return count


print(number_of_digits(432))
