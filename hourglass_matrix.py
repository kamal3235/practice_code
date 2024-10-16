# find an hourglass sum
# find max of sum


def hourglass_matrix(arr):
    max_sum = float('-inf')
    for i in range(4):
        for j in range(4):  # matrix iterate from [0][0], [1][1], [2][2], [3][3]]
            print(i, j)
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass = top + middle + bottom
            # print(hourglass)

            if hourglass > max_sum:
                max_sum = hourglass

    return max_sum









arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print(hourglass_matrix(arr))