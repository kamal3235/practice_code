


def bomberman(n, grid):
    if n == 1:
        return grid
    if n % 2 == 0:
        return ['O'* c for i in range(r)]
    n //= 2
    for q in range((n+1) % 2 +1):
        newgrid = [['O'] * c for i in range(r)]
        def set(x, y):
            if 0<=x<r and 0<=y<c:
                newgrid[x][y] = '.'
        xi = [0, 0, 0, 1, -1]
        yi = [0, -1, 1, 0, 0]
        for x in range(r):
            for y in range(c):
                if grid[x][y] == 'O':
                    for i, j in zip(xi, yi):
                        set(x+i, y+j)
        grid = newgrid
    return ["".join(x) for x in grid]

r, c, n = 6, 7, 3
grid = [
    ".......",
    "...O...",
    "....O..",
    ".......",
    "OO.....",
    "OO....."
]
result = bomberman(n, grid)
for row in result:
    print(row)