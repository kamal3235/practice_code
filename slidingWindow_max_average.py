

def find_max_average(nums, k):
    current_sum = 0
    # build the fixed window and find sum
    for i in range(k):
        current_sum += nums[i]
        # find current average as max_average
    max_average = current_sum / k

    for i in range(k, len(nums)):
        current_sum += nums[i]
        current_sum -= nums[i - k]
    # window slide to right, add right index and minus left

        avg = current_sum / k
        max_average = max(max_average, avg)
    return max_average

print(find_max_average([1, 12, -5, -6, 50, 3], 4))