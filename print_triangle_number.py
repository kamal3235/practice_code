# Abu Kamal
# can not use str
# in two line

for i in range(1, 5):
    print((10**i//9) * i)

# explanation 10**1//9 = 10//9 = 1
#               10**2//9 = 100//9 = 11 and then continue 111, 1111......
# multiply by i will make the output   1, 22, 333, 4444
# output
# 1
# 22
# 333
# 4444

# another solution

for i in range(1, 5):
    print(''.join([chr(48+i)] * i))

# chr48 = 0
# 0+i = 1

for i in range(1, 5):
    print(''.join([chr(49 + i)] * i))
print()
#  join method takes the list words and concatenates its elements into a single string,
# It takes an iterable (like a list or tuple) as an argument.
words = ['Hello', 'world', 'this', 'is', 'Python']
sentence = ' '.join(words)
print(sentence)

words = ['apple', 'banana', 'cherry']
fruits = ', '.join(words)
print(fruits)

