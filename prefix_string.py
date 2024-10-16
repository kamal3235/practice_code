


def longest_common_prefix(strs):
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[0:len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))


def longest_common_prefix1(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:len(prefix) - 1]
            if prefix == "":
                return ""
    return prefix


print(longest_common_prefix1(['leet', 'leetcode', 'leton']))

def longestCommonPrefix2(strs):
    if strs == None or len(strs) == 0:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][0:i]
    return strs[0]

print(longestCommonPrefix2(['cold', 'cool', 'colder']))
def longest_common_suffix(strs):
    if not strs:
        return ""

    suffix = strs[0]
    for i in range(1, len(strs)):
        while not strs[i].endswith(suffix):
            suffix = suffix[1:]
            if suffix == "":
                return ""
    return suffix

print(longest_common_suffix(['wonderful', 'beautiful', 'awful']))