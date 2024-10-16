Alphabets = "abcdefghijklmnopqrstuvwxyz"
def rotate(Alphabets, n):
    return Alphabets[n:] + Alphabets[:n]

print(rotate("abcdefghijklmnopqrstuvwxyz", 3))


from collections import deque

def rotate_deque(string, n):
    d = deque(string)
    d.rotate(-n)
    return "".join(d)

print(rotate_deque("HelloWorld", 2))
print()
def rotate_alphabets(s, n):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                result += alphabet[(alphabet.index(letter.lower()) + n) % 26].upper()
            else:
                result += alphabet[(alphabet.index(letter) + n) % 26]
        else:
            result += letter
    return result

print(rotate_alphabets("middle-Outz",2))


def alphabet_rotate(text, k):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    res = ""

    for c in text:
        if c.isalpha():
            shifted_letter = alphabet[(alphabet.index(c.lower()) + k) % 26]
            if c.isupper():
                res += shifted_letter.upper()
            else:
                res += shifted_letter
        else:
            res += c
    return res
print(alphabet_rotate("www.abc.xy", 87))
print()
# this is used
import string
alpha_low = string.ascii_lowercase
alpha_up = string.ascii_uppercase


def caesarCipher(s, k):
    # Write your code here

    res = []
    for c in s:
        if c.islower():
            res.append(alpha_low[(alpha_low.index(c) + k) % len(alpha_low)])
        elif c.isupper():
            res.append(alpha_up[(alpha_up.index(c) + k) % len(alpha_up)])
        else:
            res.append(c)

    return ''.join(map(str, res))


print(caesarCipher("middle-Outz", 2))