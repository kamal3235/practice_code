



def prefix(nums):
    prefix = []
    curr = 0
    for num in nums:
        curr += num
        prefix.append(curr)
    return prefix

print(prefix([1, 2, 3, 4, 5, 6, 7]))

def sum_range()