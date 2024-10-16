


def reverse_array(arr):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverse_array([1, 2, 3, 4, 5]))

def reverse_arr1(arr1):
    arr1.reverse()
    return arr1
print(reverse_arr1([5, 6, 7, 8]))

def reverse_array(array):
    n = len(array)
    temp = [0] * n
    for i in range(n):
        temp[i] = array[n - i - 1]
    for i in range(n):
        array[i] = temp[i]
    return array

print(reverse_array([7, 8, 9, 10]))


def reverse_arr2(arr2):
    n = len(arr2)
    for i in range(n // 2):
        temp = arr2[i]
        arr2[i] = arr2[n - i -1]
        arr2[n - i -1] = temp
    return arr2

print(reverse_arr2([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# recursion

def reverse_with_recursion(ar, l, r):
    if l >= r:
        return
    ar[l], ar[r] = ar[r], ar[l]
    reverse_with_recursion(ar, l+1, r-1)
    return ar

print(reverse_with_recursion([9, 8, 7, 6, 5], 0, 4))

