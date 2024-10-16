# You are given a square map as a matrix of integer strings.
# Each cell of the map has a value denoting its depth.
# We will call a cell of the map a cavity if and only if
# this cell is not on the border of the map
# and each cell adjacent to it has strictly smaller depth.
# Two cells are adjacent if they have a common side, or edge



def cavity_map(grid):
    # Write your code here
    n = len(grid)
    output = [list(row) for row in grid]
    # creates a copy of the grid, converted from a string to a list of characters. This allows us to modify individual cells.
    for i in range(1, n- 1):
        #  loop that iterates over the rows of the grid, excluding the first and last rows since border cells cannot be cavities
        for j in range(1, n - 1):
            if (grid[i][j] > grid[i - 1][j] \
                    and grid[i][j] > grid[i + 1][j] \
                    and grid[i][j] > grid[i][j - 1] \
                    and grid[i][j] > grid[i][j + 1]):
                # current cell (grid[i][j]) is greater than its adjacent cells (above, below, left, and right)
                output[i][j] = 'X'

    return [''.join(row) for row in output]
# After processing all cells, we convert each row of the result grid back to a string and return the modified grid as a list of strings.

# Example usage:
grid = [
    "1112",
    "1912",
    "1892",
    "1234"
]

modified_grid = cavity_map(grid)
for row in modified_grid:
    print(row)