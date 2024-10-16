


def count_majority(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > len(arr) // 2:
            return arr[i]
    return -1

print(count_majority([1, 1, 2, 1, 3, 5, 1]))
print()








