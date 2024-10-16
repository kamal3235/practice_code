



def insertionsort1(start, arr):
    probe = arr[start]
    changed = 0
    for i in range(start - 1, -1, -1):
        if arr[i] > probe:
            changed += 1
            arr[i + 1] = arr[i]
            # print(probe, start, arr)
        else:
            arr[i + 1] = probe

            break

    return changed
def insertionsort2(n, arr):
    res = 0
    for i in range(1, len(arr)):
        res += insertionsort1(i, arr)
        print((' '.join(map(str, arr))))
    return res
def runningtime(arr):
    return insertionsort2(len(arr), arr)

print(runningtime([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


def shift_insertion1(arr):
    shifts = 0
    for i in range(1,len(arr)):
        j = i
        while j >= 1 and arr[j] < arr[j-1]:
            shifts += 1
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return shifts

print(shift_insertion1([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))


def quickSort(arr):
    left = []
    equal = []
    right = []
    pivot = arr[0]

    for el in arr:
        if el < pivot:
            left.append(el)
        elif el == pivot:
            equal.append(el)
        elif el > pivot:
            right.append(el)

    return left + equal + right

print(quickSort([4, 5, 3, 7, 2]))

number = [1 2 3 4 5 6]
arr =