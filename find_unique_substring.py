

# create a function that generates all possible substrings
# of a given string and stores them
# in a set to ensure uniqueness.
def unique_substrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+ 1):
            substrings.add(s[i:j])
    return substrings

print(unique_substrings("aab"))
print(unique_substrings("aac"))
def kth_in_sub_string(s1, s2, k):
    x = unique_substrings(s1)
    y = unique_substrings(s2)
    z = sorted(x.union(y))
    if k <= len(z):
        return z[k-1]
    else:
        return None


s1 = "aab"
s2 = "aac"
k = 8
res = kth_in_sub_string(s1, s2, k)
print(res)
print()
print()

# findStrings has the following parameter(s):
# w: an array of strings
# queries: an array of integers
def unique_substring(s):
    sub_strings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub_strings.add(s[i:j])
    return sub_strings

# function combines the unique substrings
# from all strings in w and sorts them.
def preprocess_substring(w):
    combined_string = set()
    for s in w:
        combined_string.update(unique_substring(s))

    sorted_sub = sorted(combined_string)
    print(sorted_sub)
    return sorted_sub


def findStrings(w, queries):
    sorted_sub = preprocess_substring(w)
    res = []
    for k in queries:
        if k <= len(sorted_sub):
            res.append(sorted_sub[k - 1])
        else:
            res.append("INVALID")
    return res

w = ["aab", "aac"]
queries = [1, 3, 8, 23]
res = findStrings(w, queries)
print(res)  # Output: ['a', 'aab', 'c', 'INVALID']