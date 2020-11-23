#1
def financialCrisis(roadRegister):
    t = 0
    matrix_list = []
    while t < len(roadRegister):
        new_matrix = []
        for idx, el in enumerate(roadRegister):
            if idx != t:
                new_matrix.append([])
                for another_idx, another_el in enumerate(el):
                    if another_idx != t:
                        new_matrix[len(new_matrix)-1].append(another_el)
        matrix_list.append(new_matrix)
        t += 1
    return matrix_list


print(financialCrisis([[False, True, True, False],
                       [True, False, True, False],
                       [True, True, False, True],
                       [False, False, True, False]]))


#2
def namingRoads(roads):
    roads_dict = {el[2]: el[:2] for el in roads}
    for i in range(len(roads)):
        if i+1 < len(roads):
            for j in roads_dict[i]:
                if j in roads_dict[i+1]:
                    return False
    return True


print(namingRoads([[0, 1, 0],
                   [4, 1, 2],
                   [4, 3, 4],
                   [2, 3, 1],
                   [2, 0, 3]]))
