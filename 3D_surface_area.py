# board showing the values of  and that the price of the toy is equal to the 3d surface area
# find the price of the toy


def surface_area(A):
    # Write your code here
    H = len(board)
    W = len(board[0])
    area = 2 * H * W

    def check(i, j):
        return A[x+i][y+j] if 0 <= x + i < H and 0 <= y + j < W else 0

    xi = [0, 0, 1, -1]
    yi = [1, -1, 0, 0]

    for x in range(H):
        for y in range(W):
            for i, j in zip(xi, yi):
                area += max(0, A[x][y] - check(i, j))
    return area


board = [
    [1, 3, 4],
    [2, 2, 3],
    [1, 2, 4]
]
print(surface_area(board))