


def unique_num(nums):
    insertindex = 1
    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            nums[insertindex] = nums[i]
            insertindex += 1
    return insertindex

print(unique_num([1,1,2]))


def removeDuplicates(nums):
    """
    nums =  doesn't replace elements in the original list.
    nums[:] = replaces element in place
    """
    nums[:] = sorted(set(nums))
    return len(nums)
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# two pointer

def unique_array(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1

print(unique_array([0,0,1,1,1,2,2,3,3,4]))


# while loop
def remove_duplicate(nums):
    slow, fast = 0, 1
    while fast in range(len(nums)):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            nums[slow+1] = nums[fast]
            fast += 1
            slow += 1
    return slow + 1
