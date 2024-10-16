


def getconcatenation_array(nums):
    nums.extend(nums)
    return nums

print(getconcatenation_array([1, 2, 3]))

def adding_array(nums):
    return nums + nums

print(adding_array([1, 2]))


def add_array(nums):
    for i in range(0, len(nums), 1):
        nums.append(nums[i])
    return nums
print(add_array([4, 5, 6]))