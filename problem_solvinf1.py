# two array of same size and target

def add_from_two_array(arr1, arr2, target):
    dict = {}
    for i, num in enumerate(arr1):
        dict[num] = i
    for j, num in enumerate(arr2):
        complement = target -num
        if complement in dict:
            return dict[complement], j

print(add_from_two_array([-1, 3, 8, 2, 9, 5], [4, 1, 2, 10, 5, 20], 29))


def find_closest_pair(ar1, ar2, target):
    closest_pair = None
    closest_diff = float('inf')
    closest_ind = (-1, -1)
    mydict = {num: i for i, num in enumerate(ar1)}
    for j, num2 in enumerate(ar2):
        for num1 in mydict:
            current_sum = num1 + num2
            curr_diff = abs(current_sum - target)
            if curr_diff < closest_diff:
                closest_diff = current_sum
                closest_pair = (num1, num2)
                closest_ind = (mydict[num1], j)
    return closest_pair, closest_ind

print(find_closest_pair([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 10))


