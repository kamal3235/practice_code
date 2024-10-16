
# leetcode 167, 15, 11
# input array sorted
# 3 sum
# container with most water



def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

print(is_palindrome("abcdcba"))


def findMaxLength(nums):
    diff = {}
    count = 0
    res = 0

    for i, n in enumerate(nums):
        count += 1 if n == 1 else -1

        if count not in diff:
            diff[count] = i

        if count == 0:
            res = i + 1
        else:
            res = max(res, i - diff[count])

    return res

print(findMaxLength([0, 1, 0]))

def two_sum(arr, target):
    start = 0
    end = len(arr) - 1
    while start < end:
        num = arr[start] + arr[end]
        if num == target:
            return [start, end]
        elif num < target:
            start += 1
        else:
            end -= 1

print(two_sum([2, 3, 4, 5, 6], 9))


def two_sum_with_dict(array, target):
    dic = {}
    for i, num in enumerate(array):
        if (target - num) in dic:
            return [dic[target-num], i]
        dic[num] = i

print(two_sum_with_dict([5, 6, 7, 8], 13))