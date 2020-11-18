#1
# def newRoadSystem(roadRegister):
#     roads_dict = {}
#     for i in range(len(roadRegister)):
#         for j in range(len(roadRegister[i])):
#             if j not in roads_dict:
#                 roads_dict[j] = [0, 0]
#             if roadRegister[i][j] == True:
#                 roads_dict[i][0] += 1
#                 roads_dict[j][1] += 1
#     if False in list(map(lambda x: False if x[0] != x[1] else True, roads_dict.values())):
#         return False
#     return True
#
#
# print(newRoadSystem([[False, True, False, False, False, False, False],
#                      [True, False, False, False, False, False, False],
#                      [False, False, False, True, False, False, False],
#                      [False, False, True, False, False, False, False],
#                      [False, False, False, False, False, False, True],
#                      [False, False, False, False, True, False, False],
#                      [False, False, False, False, False, True, False]]))


#2
def there_is_a_way_from_A_to_B(a, b, roads):
    if [a, b] in roads or [b, a] in roads:
        return True
    return False


def efficientRoadNetwork(n, roads):
    for i in range(n):
        for j in range(i + 1, n):
            if not there_is_a_way_from_A_to_B(i, j, roads):
                new_roads = list(filter(lambda x: i in x, roads))
                for el in new_roads:
                    if there_is_a_way_from_A_to_B(el[0] if el[1] == i else el[1], j, roads):
                        break
                else:
                    return False
    return True


print(efficientRoadNetwork(5, [[3, 0],
                               [0, 4],
                               [5, 0],
                               [2, 1],
                               [1, 4],
                               [2, 3],
                               [5, 2]]))
