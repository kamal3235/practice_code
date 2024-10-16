


def anagram_function(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s)//2
    s1 = s[:mid]
    s2 = s[mid:]
    count_s1 = [0] * 26
    count_s2 = [0] * 26

    for char in s1:
        count_s1[ord(char) - ord('a')] += 1

    for char in s2:
        count_s2[ord(char) - ord('a')] += 1

    changes = 0
    for i in range(26):
        if count_s1[i] > count_s2[i]:
            changes += count_s1[i] - count_s2[i]

    return changes
s = 'aaabbb'
print(anagram_function(s))

from collections import Counter
def count_changes_anagram(s):
    if len(s)%2 != 0:
        return -1

    mid = len(s) // 2
    a = s[:mid]
    b = s[mid:]
    count_a = Counter(a)
    count_b = Counter(b)
    # print(count_a, count_b)
    changes = 0
    for char in count_a:
        if count_a[char] > count_b[char]:
            
            changes += count_a[char] - count_b[char]
    return changes




print(count_changes_anagram('xyyx'))