def numbers(n):
    a = 1
    b = 10
    for i in range(2, n + 1):
        if i >= b:
            b *= 10
        a *= b
        a += i
    return a


print(numbers(13))