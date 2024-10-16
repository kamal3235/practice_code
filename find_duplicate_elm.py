
# find duplicate elem in array

def find_duplicate_elm(arr):
    res = []
    for i in range(len(arr) -1):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                if arr[i] not in res:
                    res.append(arr[i])
    return res

print(find_duplicate_elm([12, 11, 40, 12, 5, 6, 5, 11]))

from collections import defaultdict

def find_duplicates(arr):
    freq = defaultdict(int)
    for x in arr:
        freq[x] += 1
    res = [x for x in freq if freq[x] > 1]
    return res

print(find_duplicates([12, 11, 40, 12, 5, 6, 5, 12, 11, 40]))
