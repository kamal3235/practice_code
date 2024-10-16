
# return True, if two elm within window
# of size k that are equal

def sliding_window(nums, k):
    for L in range(len(nums)):
        for R in range(L+1, min(len(nums), L+k)):
            if nums[L] == nums[R]:
                return True
    return False

print(sliding_window([1, 2, 3, 2, 3, 3], 2))



# def sliding_window_On(nums, k):
#     window = set()
#     L = 0
#     for R in range(len(nums)):
#         if R - L + 1 > k:
#             window.remove(nums[L])
#             L += 1

# Find longest subarray of same num
def longest_subarray(nums):
    length = 0
    L = 0
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        length = max(length, R - L + 1)
    return length


print(longest_subarray([4, 2, 2, 3, 3, 3]))

# Find minimum length subarray
# where sum is greater or equal to target

def shortest_subarray(nums, target):
    curr_sum = 0
    L = 0
    length = float('inf')
    for R in range(len(nums)):
        curr_sum += nums[R]
        while curr_sum >= target:
            length = min(length, R - L + 1)
            curr_sum -= nums[L]
            L += 1
    return 0 if length == float('inf') else length

print(shortest_subarray([2, 3, 1, 2, 4, 3], 6))


