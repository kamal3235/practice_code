# a password to be strong if it satisfies the following criteria:
#
# Its length is at least .
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character
# count missing requirments

import re
def correct_password(n, password):   # n = len(password)
    p = [ "[A-Z]", "[a-z]", "[\\d]", "[!@#$%^&*()-+]"]
    return max(6-n, sum(1 for i in p if not re.search(i, password)))


print(correct_password(7, "AUzs-nV"))
# fail to read "-" in one test cases

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def minimum_number(n, password):
    res = 0
    if not any(x in numbers for x in password):
        res += 1
    if not any(x in lower_case for x in password):
        res += 1
    if not any(x in upper_case for x in password):
        res += 1
    if not any(x in special_characters for x in password):
        res += 1
    if len(password) < 6:
        return max(res, 6 - len(password))
    return res

print(minimum_number(7, "AUzs-nV"))




a = (("this", "is"), ("a", "contrived", "example"), ("of", "the", "caboose", "idiom"))
for b in a:
    for c in b:
        if "is" == c:
            break
        else:
            print(c)
