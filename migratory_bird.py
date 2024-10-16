
# find higest freq

def migratory_bird(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    # Finding the key with max value
    max_count = max(freq.values())
    most_freq_type = [type for type, count in freq.items() if count == max_count]

    return min(most_freq_type)

print(migratory_bird([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))

from collections import Counter

def count_freq_bird_type(array):
    freq = Counter(array)
    return freq

print(count_freq_bird_type([1, 4, 4, 4, 5, 3]))
print()
arr = [1, 4, 4, 4, 5, 3]
bird_count = {}
for bird in arr:
    if bird in bird_count:
        bird_count[bird] += 1
    else:
        bird_count[bird] = 1
print(arr)
print(bird_count)
max_count = max(bird_count.values())
max_type = max(bird_count.keys())
print(max_count)
print(max_type)
most_freq = [bird for bird, count in bird_count.items() if count == max_count]
print(most_freq)

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = {}
for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print(freq)

students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'A'},
    {'name': 'David', 'grade': 'C'}
]

group_by_grade = {}

for student in students:
    grade = student['grade']
    if grade not in group_by_grade:
        group_by_grade[grade] = []
    group_by_grade[grade].append(student['name'])

print(group_by_grade)