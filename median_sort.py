# numbers = []
# line = "39 46 61 44"
# numbers.extend(map(int, line.split()))
# print(numbers)  # Output: [39, 46, 61, 44]
# numpy array is more efficient then list in big data
# extend add to the list, append add as new list

import numpy as np

def read_integers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = []
        for line in file:
            numbers.extend(map(int, line.split()))

        return np.array(numbers)
def median(numbers):
    return np.median(numbers)




file_path = 'numbers.txt'
numbers = read_integers_from_file(file_path)
find_median = median(numbers)
print(f'the median is: {find_median}')