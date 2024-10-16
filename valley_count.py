


# find D and U
# find level
def valley_count(s):
    count = 0
    count_vally = 0
    for i in range(len(s)):
        if s[i] == "U":
            count -= 1
            if count == 0:
                count_vally += 1
        elif s[i] == "D":
            count += 1

    return count_vally

print(valley_count('DDUUDDUDUUUD'))