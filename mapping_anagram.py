


def mapping_anagram(nums1, nums2):
    dict = {}
    for num in range(len(nums2)):
        dict[nums2[num]] = num
        print(dict)

    for num in nums1:
        if num in dict:
            return [dict[num] for num in nums1]

print(mapping_anagram([12,28,46,32,50], [50,12,32,46,28]))

my_iterable = range(1, 3)
my_iterator = my_iterable.__iter__()
print(my_iterator.__next__())
print(my_iterator.__next__())
# print(my_iterator.__next__())

mystring = "ABC"
for letter in mystring:
    print(letter)
mylist = ['A', 'B', 'C']
for letter in mylist:
    print(letter)

# comprehension
print(([x for x in 'ABC']))
print([x for x in [1, 2, 3, 4] if x > 2])
print()
mydict = {'name': 'Alice', 'age': 23, 'country': 'USA'}
for i in mydict:
    print(i)
print()
for i in mydict.values():
    print(i)

for k, v in mydict.items():
    print(k, v)
    
with open('numbers.txt') as numbers:
    for line in numbers:
        process_number(line)