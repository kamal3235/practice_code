


def birthday_chocolate_share(s, d, m):

    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count += 1

    return count

print(birthday_chocolate_share([5, 1, 4, 1, 5, 4, 5, 1, 3, 5, 1, 1, 5, 1, 4, 2, 1, 1, 1, 2, 5], 15, 7))

# sliding window

def chocolate_share_sliding(s, d, m):
    count = 0
    current_sum = sum(s[:m])

    if current_sum == d:
        count += 1

    for i in range(m, len(s)):
        current_sum += s[i] - s[i - m]
        print(i, current_sum)
        if current_sum == d:
            count += 1
    return count

# Initial Window:
    # Elements: [2, 2]
    # current_sum = 4
# Check: current_sum == d (True, so count = 1)
# First Slide:
    # New Element: 1 (at index 2)
    # Remove Element: 2 (at index 0)
    # Update: current_sum += 1 - 2 → current_sum = 4-2 = 3
    # Check: current_sum == d (False)
# Second Slide:
    # New Element: 3 (at index 3)
    # Remove Element: 2 (at index 1)
    # Update: current_sum += 3 - 2 → current_sum = 3 + 1 = 4
    # Check: current_sum == d (True, so count = 2)
# Third Slide:
    # New Element: 2 (at index 4)
    # Remove Element: 1 (at index 2)
    # Update: current_sum += 2 - 1 → current_sum = 4 + 1 = 5
    # Check: current_sum == d (False)

print(chocolate_share_sliding([2, 2, 1, 3, 2], 4, 2))