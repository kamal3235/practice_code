


def mini_cost(s):

    poss_magic = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    min_cost = float('inf')
    for p in poss_magic:
        curr_cost = 0
        for i in range(len(p)):
            for j in range(len(p[i])):
                curr_cost += abs(s[i][j] - p[i][j])

        if curr_cost < min_cost:
            min_cost = curr_cost
    return min_cost


s = [[4, 8, 2],[4, 5, 7],[6, 1, 6]]
print(mini_cost(s))

# using flatten square
def forming_magic_square(s):
    magic_squares = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8]
    ]
    # make s flat to compare with magic
    s_flat = [item for sublist in s for item in sublist]    # OR s = sum(s, [])
    min_cost = float('inf')

    for magic in magic_squares:
        cost = sum(abs(s_flat[i] - magic[i]) for i in range(9))
        min_cost = min(min_cost, cost)

    return min_cost


# Example usage
s = [
    [4, 8, 2],
    [4, 5, 7],
    [6, 1, 6]
]

print(forming_magic_square(s))  # Output: 4
print()

def formingMagicSquare(s):
    # Write your code here
    # flatten the s to compare with magic
    s = sum(s, [])
    magic = [[6, 7, 2, 1, 5, 9, 8, 3, 4], \
             [8, 3, 4, 1, 5, 9, 6, 7, 2], \
             [2, 7, 6, 9, 5, 1, 4, 3, 8], \
             [4, 3, 8, 9, 5, 1, 2, 7, 6], \
             [2, 9, 4, 7, 5, 3, 6, 1, 8], \
             [4, 9, 2, 3, 5, 7, 8, 1, 6], \
             [6, 1, 8, 7, 5, 3, 2, 9, 4], \
             [8, 1, 6, 3, 5, 7, 4, 9, 2]]

    min_cost = float("Inf")

    for p in magic:
        curr_cost = 0
        for i, j in zip(s, p):
            curr_cost += abs(i - j)

        min_cost = min(min_cost, curr_cost)
    return min_cost


print(formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))