# kadane algorithm
# max sum of subarray in O(n) time
#




def max_subarray_sum(arr):
    res = arr[0]
    max_ending = arr[0]
    for i in range(1, len(arr)):
        max_ending = max(max_ending + arr[i], arr[i])
        res = max(res, max_ending)
    return res

print(max_subarray_sum([2, 3, -8, 7, -1, 2, 3]))

# print the sunarray with max+sum

def max_subarray(array):
    res_start = 0
    res_end = 0
    curr_start = 0
    max_sum = array[0]
    max_ending = array[0]

    for i in range(1, len(array)):
        if max_ending + array[i] < array[i]:
            max_ending = array[i]
            curr_start = i
        else:
            max_ending += array[i]
            print(max_ending, curr_start)

        if max_ending > max_sum:
            max_sum = max_ending
            res_start = curr_start
            res_end = i
    res = array[res_start:res_end+1]
    return res

print(max_subarray([2, 3, -8, 7, -1, 2, 3]))