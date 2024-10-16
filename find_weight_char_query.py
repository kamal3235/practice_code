


def weighted_uniform_string(s, queries):
    weights = set()
    current_char = ''
    current_weight = 0

    for char in s:
        if char == current_char:
            current_weight += ord(char) - ord('a') + 1
        else:
            current_char = char   # char is different from current_char, update current
            current_weight = ord(char) - ord('a') + 1
        weights.add(current_weight)
        print(char)
        print(weights)
    res = []
    for query in queries:
        if query in weights:
            res.append('Yes')
        else:
            res.append('No')
    return res

print(weighted_uniform_string("abccddde", [6, 1, 3, 12, 5, 9, 10]))


