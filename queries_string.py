# input string
# query string
# how many times it occur
# dict.get()
from collections import defaultdict


def matching_string(arr, queries):
    seen = {}
    for string in arr:
        if string in seen:
            seen[string] += 1
        else:
            seen[string] = 1
    res = []
    for query in queries:
        res.append(seen.get(query, 0))
    return res


print(matching_string(["ab", "ab", "abc"], ['ab', 'abc', 'bc']))


def matching_string2(stringlist, queries):
    freq = defaultdict(int)
    res = []
    for string in stringlist:
        freq[string] += 1
    for query in queries:
        if query in freq:
            res.append(freq[query])
        else:
            res.append(0)
    return res
print(matching_string2(["ab", "ab", "abc"],['ab', 'abc', 'bc'] ))



def matching_string3(array, queries):
    q = []
    for i in queries:
        if i in array:
            q.append(array.count(i))
        else:
            q.append(0)
    return q

print(matching_string3(["ab", "ab", "abc"],['ab', 'abc', 'bc']))

def matching_string4(arr, queries):
    result = [0 for i in range(len(queries))]
    # This line creates a list called results with the same length as queries
    for i, query in enumerate(queries, 0):   # starts the index at 0
        for j in range(len(arr)):
            if query == arr[j]:
                result[i] += 1
    return result

print(matching_string4(["ab", "ab", "abc"],['ab', 'abc', 'bc']))


freq = {'apple': 3, "banana": 2}
count = freq.setdefault('grape', 0)
print(freq.values())


from collections import defaultdict

frequency = defaultdict(int)
frequency["apple"] += 1  # Automatically initializes "apple" with 0 and then increments
print(frequency["apple"])  # Output: 1
print(frequency["banana"])  # Output: 0 (default value for int)

# HOW CODE WORKS

# for i, query in enumerate(queries, 0):
#     for j in range(len(stringList)):
#         if query == stringList[j]:
#             results[i] += 1


# queries = ["apple", "banana", "grape"]
# stringList = ["apple", "orange", "banana", "apple"]
#
# First Query (“apple”):
# i = 0, query = "apple"
# Inner loop:
# j = 0, stringList[0] = "apple" -> results[0] += 1 -> results = [1, 0, 0]
# j = 1, stringList[1] = "orange" -> No match
# j = 2, stringList[2] = "banana" -> No match
# j = 3, stringList[3] = "apple" -> results[0] += 1 -> results = [2, 0, 0]

# Second Query (“banana”):
# i = 1, query = "banana"
# Inner loop:
# j = 0, stringList[0] = "apple" -> No match
# j = 1, stringList[1] = "orange" -> No match
# j = 2, stringList[2] = "banana" -> results[1] += 1 -> results = [2, 1, 0]
# j = 3, stringList[3] = "apple" -> No match

# Third Query (“grape”):
# i = 2, query = "grape"
# Inner loop:
# j = 0, stringList[0] = "apple" -> No match
# j = 1, stringList[1] = "orange" -> No match
# j = 2, stringList[2] = "banana" -> No match
# j = 3, stringList[3] = "apple" -> No match

# Final Results   2, 1, 0

def matchingStrings5(stringList, queries):
    # Write your code here
    res = []

    for i, query in enumerate(queries):
        for j in range(len(stringList)):
            if query == stringList[j]:
                res.append(stringList.count(j))
    return res

print(matchingStrings5(["ab", "ab", "abc"],['ab', 'abc', 'bc']))