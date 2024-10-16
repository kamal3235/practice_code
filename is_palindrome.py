# Two pointer problem



def is_palindrome(word):
    L, R = 0, len(word) -1    # indexing
    while L < R:
        if word[L] != word[R]:
            return False
        L += 1
        R -= 1
    return True

print(is_palindrome('abcddcba'))
print(is_palindrome([1, 2, 3, 4, 4, 3, 2, 1]))

# Given a sorted array
# return indices of two elm in different position
# that sum up to Target value

def target_sum(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            return [L, R]

print(target_sum([-1, 2, 3, 4, 7, 9], 7))