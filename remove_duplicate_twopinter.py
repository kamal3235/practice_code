


def remove_duplicate(nums):
    slow, fast = 0, 1
    while fast in range(len(nums)):
        if nums[slow] == nums[fast]:
            fast += 1
        else:   # if not equel, fast move to the popsition of slow+1
            nums[slow+1] = nums[fast]
            fast += 1
            slow += 1
    return slow + 1


print(remove_duplicate([1, 1, 2]))
print()
def remove_duplicate_simple(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
            print(i, j, nums[i], nums[j])
    return  nums, j+1

print(remove_duplicate_simple([1, 2, 2, 2, 3, 5, 6]))
print()

def remove_duplicate_popmethod(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

print(remove_duplicate_popmethod([1, 2, 2, 3, 3, 4]))


from collections import OrderedDict

def remove_duplicate_orderdict(nums):
    nums[:] = OrderedDict.fromkeys(nums)
    return len(nums)

print(remove_duplicate_orderdict([1, 2, 3, 3, 3, 4, 8]))