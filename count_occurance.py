

def occurance(arr, x):
    res = 0
    for i in range(len(arr)):
        if x == arr[i]:
            res += 1
    return res





arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(occurance(arr, x))


# binary search of first occurance
# binary search for last occurance

def first_occurance(arr, l, h, x):
    arr = sorted(arr)
    if h >= l:
        mid = (l + h) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first_occurance(arr, mid+1, h, x)
        else:
            return first_occurance(arr, l, mid-1, x)
    return -1


def last_occurance(arr, n, l, h, x):
    if h >= l:
        mid = (l+h) // 2
        if (mid == n or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return last_occurance(arr, n, l, mid-1, x)
        else:
            return last_occurance(arr, n, mid + 1, h, x)
    return -1


def count_occurance(arr, n, x):
    index_first = first_occurance(arr, 0, n - 1, x)
    if index_first == -1:
        return -1
    index_last = last_occurance(arr, n, index_first, n-1, x)

    return index_last - index_first + 1

print(count_occurance([1, 1, 2, 2, 2, 2, 3], 7, 2))








