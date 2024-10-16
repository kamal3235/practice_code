



def marsExploration(s):
    # Write your code here
    expected_mess = "SOS"

    # find the difference
    count = 0
    for i in range(len(s)):
        if s[i] != expected_mess[i % 3]:

            count += 1
    return count

print(marsExploration("SOSOOSOSOSOSOSSOSOSOSOSOSOS"))
print()
def count_sos_message(s):
    res = 0
    for i in range(0, len(s), 3):
        print(i)
        if s[i] != "S":
            res += 1
        if s[i+1] != "O":
            res += 1
        if s[i+2] != "S":
            res += 1
    return res

print(count_sos_message("SSSSSSSSSSSSSSSOOOOOOOOOOOOOOOOOOOOOOOOOSSSSSSSO"))