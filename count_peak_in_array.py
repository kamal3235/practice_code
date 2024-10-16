


def count_peak(array):
    count = 0
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            count += 1
    return count

print(count_peak([1, 2, 3, 1, 5, 6, 4]))