def buildPalindrome(string):
    for el in string:
        if string[-(string.find(el)+1)] != el:
            if string.find(el) == 0:
                string = string[:] + el
            else:
                string = string[:-(string.find(el))] + el + string[-(string.find(el)):]
    return string


print(buildPalindrome("abcdc"))
