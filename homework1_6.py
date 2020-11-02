#1
def swap_list_elements(list):
    a = ''
    for i in range(len(list)):
        if i % 2 == list[i] % 2:
            continue
        else:
            if a == '':
                a = i
            else:
                list[a], list[i] = list[i], list[a]
                a = ''
    return list
print(swap_list_elements([1, 4, 6, 5, 7, 10]))

