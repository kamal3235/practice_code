


def vowel_change(s):
    vowel = "aeiou"
    count_chnage = 0
    prevoius_char = None
    for char in s:
        if char in vowel:
            if prevoius_char and prevoius_char != char:
                count_chnage += 1
            prevoius_char = char
    return count_chnage

print(vowel_change("aeiou"))
print(vowel_change("hello World"))