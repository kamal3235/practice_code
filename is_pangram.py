import string


def pangrams(s):
    # Write your code here
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    s = s.lower()
    s = set(s)
    if alphabets.issubset(s):
        return "pangram"
    return "not pangram"

print(pangrams("We promptly judged antique ivory buckles for the next prize"))

def is_pangram(s):
    s = s.lower()
    ispangram = True
    for letter in string.ascii_lowercase:
        ispangram = ispangram and letter in s
    if ispangram:
        return "pangram"
    return "not pangram"


print(is_pangram("NOVmETKPTbYu ftZPEykhjgF GGkdGjWGwW skjPJsea dtwdqcr DERCUgxOxrRgDQbdzL IZjyXs"))