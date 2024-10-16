# check leetcode 303, 525, 560


def find_subarray_sum(array, i, j):
    subarray_sum = 0
    for k in range(i, j+1):
        subarray_sum += array[k]
        # print(k, array[k])
    return subarray_sum

print(find_subarray_sum([7, 9, 11, 13, 19], 1, 3))
print()
def create_prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr

print(create_prefix_sum([1, 2, 3, 4, 5]))
print()
def picking_number(arr):
    arr = sorted(arr)
    longest_subarray = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if abs(arr[i]- arr[j]) <= 1:
                longest_subarray = max(longest_subarray, j - i + 1)

    return longest_subarray

print(picking_number([1, 1, 2, 2, 4, 4, 5, 5, 5]))
print(picking_number([1, 2, 2, 3, 1, 2]))
print()

from collections import Counter

# remember its a dictionary object d, key is the element and value
# how many times it appear in the array
# max(d[i] + d[i+1] refer to the consecutive number keys
# as such the range is 99
def longest_subarray(a):
    d = Counter(a)
    print(d)
    best = 0
    for i in range(99):
        best = max(d[i] + d[i+1], best)
    return best


print(longest_subarray([4, 6, 5, 3, 3, 1]))
print(longest_subarray([1, 2, 2, 3, 1, 2]))
print(longest_subarray([1, 1, 2, 2, 4, 4, 5, 5, 5]))
