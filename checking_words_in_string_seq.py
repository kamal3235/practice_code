


def hackerrankInString(s):
    # Write your code here
    word = "hackerrank"
    j = 0
    for letter in s:
        if letter == word[j]:
            j += 1
        if j == len(word):
            return "YES"
    return "NO"

print(hackerrankInString("hereiamstackerrank"))
import re
def hackerrank_in_string(s):
    return "YES" if re.search(".*".join(list("hackerrank")), s) else "NO"

print(hackerrank_in_string("hackerworld"))