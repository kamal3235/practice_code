


def anagram_eval(s):
    if len(s) % 2 != 0:
        return -1
    else:
        sub1 = list(s[len(s)//2:])
        for i in s[:len(s)//2]:
            if i in sub1:
                sub1.remove(i)
        return len(sub1)

print(anagram_eval('abbc'))


def anagram_with_collections(s):
    if len(s) % 2:
        return -1
    from collections import Counter
    c1 = Counter(s[:len(s)//2])
    c2 = Counter(s[len(s)//2:])

    return (c2 - c1).total()

print(anagram_with_collections('abbc'))

def anagram(s):
    if len(s)%2 != 0:
        return -1
    else:
        split = len(s)//2
        s1 = s[:split]
        s2 = s[split:]
        for i in s1:
            if i in s2:
                s1 = s1.replace(i,'',1)
                s2 = s2.replace(i,'',1)
        return len(s1)

print(anagram('abbc'))

# str.replace(old, new[, count])
text = "hello world"
new_text = text.replace("world", "Python")
print(new_text)  # Output: "hello Python"

text = "banana"
new_text = text.replace("a", "o", 2)
print(new_text)  # Output: "bonona"