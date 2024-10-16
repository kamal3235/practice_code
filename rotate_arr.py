# Store the last element in any temp variable
# Shift every element one position ahead
# Assign first value = last value (stored in temp variable).


def rotate_array(arr):
    n = len(arr)
    last_el = arr[n -1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_el
    return arr
# Look how it works, assign var to last_el
# arr[4] = arr[3]
#   arr[ ] = {1, 2, 3, 4, 4}
# arr[3] = arr[2]
#   arr[ ] = {1, 2, 3, 3, 4}
# arr[2] = arr[1]
#   arr[ ] = {1, 2, 2, 3, 4}
# arr[1] = arr[0]
#   arr[ ]  = {1, 1, 2, 3, 4}
# give back last elm



print(rotate_array([1, 2, 3, 4, 5]))


# next solution
# two pointer

def rotate_arr(arr1):
    n = len(arr1)
    left = 0
    right = n - 1
    while left != right:
        arr1[left], arr1[right] = arr1[right], arr1[left]
        left += 1
        pass

    return arr1

print(rotate_arr([6, 7, 8, 9]))

def rotation_by_num(d, arr):
    return arr[d:] + arr[:d]

print(rotation_by_num(4, [1, 2, 3, 4, 5]))

# using for loop
def rotate_array_by_num(d, arr):
    n = len(arr)
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[(i + d) % n]   # (i + d) % n cal new index
        # temp[0] = arr[(0 + 2) % 6] = arr[2] = 3
        # temp = [3, 0, 0, 0, 0, 0]
        # temp[5] = arr[(5 + 2) % 6] = arr[1] = 2
        # temp = [3, 4, 5, 6, 1, 2]
    for i in range(n):
        arr[i] = temp[i]
    return arr

print(rotate_array_by_num(2, [1, 2, 3, 4, 5, 6]))