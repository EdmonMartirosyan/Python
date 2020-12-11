#1
def strings(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))


print(strings("abvdj", "vjdab"))


#2
def search(matrix, number):
    for i in range(len(matrix)):
        j = 0
        k = len(matrix) - 1
        while j <= k:
            mid = (j + k) // 2
            if matrix[i][mid] < number:
                j = mid + 1
            elif matrix[i][mid] > number:
                k = mid - 1
            else:
                return i, mid


print(search([[10, 20, 30, 40],
              [15, 25, 35, 45],
              [27, 29, 37, 48],
              [32, 33, 39, 50]], 29))
