# Abu Kamal
# funding substring with or without vowel
# list comprehension


def minion_game(string):
    # your code goes here
    scores = {"Kevin": 0, "Stuart": 0}
    for i in range(len(string)):
        if string[i] in "AEIOU":
            scores["Kevin"] += len(string) - i

        else:
            scores["Stuart"] += len(string) - i

    if scores["Kevin"] > scores["Stuart"]:
        print(f"Kevin {scores["Kevin"]}")
    elif scores["Stuart"] > scores["Kevin"]:
        print(f"Stuart {scores["Stuart"]}")
    else:
        print("Draw")

print(minion_game("BANANA"))
print()

s = "BANANA"
print(s)
print(len(s))
print(s[0])
vowels = 'AEIOU'
vowel_substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if s[i] in vowels]
print(vowel_substrings)
print(len(vowel_substrings))
constant_substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if s[i] not in vowels]
print(constant_substrings)
print(len(constant_substrings))
print()


def stuart_substrings(string):
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    length = len(string)
    stuart_subs = []

    for i in range(length):
        if string[i] in consonants:
            for j in range(i + 1, length + 1):
                stuart_subs.append(string[i:j])

    return stuart_subs

print(stuart_substrings("BANANA"))