

def absolute_permutation(n, k):
    if k == 0:
        return list(range(1, n+1))
    cache = set(range(1, n+1))
    res = []
    for i in range(1, n+1):
        lower = i - k
        upper = i + k
        if lower in cache:
            cache.remove(lower)
            res.append(lower)
        elif upper in cache:
            cache.remove(upper)
            res.append(upper)
        else:
            return [-1]
    return res

print(absolute_permutation(4, 2))