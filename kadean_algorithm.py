

# O(n^2)
def max_sum_nonempty_array(nums):
    max_sum = nums[0]

    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            # print(i, j, curr_sum)
            max_sum = max(max_sum, curr_sum)
    return max_sum

print(max_sum_nonempty_array([4, -1, 2, -7, 3, 4]))

# O(n)
def kadens_max_sum(arr):
    max_sum = arr[0]
    curr_sum = 0

    for num in arr:
        curr_sum = max(curr_sum, 0)   # ensures that we reset the current sum to 0 if it becomes negative
        curr_sum += num
        print(num, curr_sum)
        max_sum = max(max_sum, curr_sum)
    return max_sum



print(kadens_max_sum([4, -1, 2, -7, 3, 4]))

def sliding_window(nums):
    max_sum = nums[0]
    curr_sum = 0
    maxL, maxR = 0, 0
    L = 0
    for R in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            L = R

        curr_sum += nums[R]
        if curr_sum > max_sum:
            max_sum = curr_sum
            maxL, maxR = L, R
    return [maxL, maxR]

print(sliding_window([4, -1, 2, -7, 3, 4]))