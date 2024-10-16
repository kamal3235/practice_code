

def is_alternating(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return False
    return True


def alternating_character(s):
    unique_char = set(s)
    max_length = 0


    for char1 in unique_char:
        for char2 in unique_char:

            if char1 != char2:

                filtered = [c for c in s if c== char1 or c == char2]

                if is_alternating(filtered):

                    max_length = max(max_length, len(filtered))
    return max_length


print(alternating_character("beabeefeab"))