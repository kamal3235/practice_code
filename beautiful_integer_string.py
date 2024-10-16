


def is_beautiful(s):

    n = len(s)
    for length in range(1, n//2+1):
        first_num = int(s[:length])
        curr_num = first_num
        index = length
        beautiful = True


        while index < n:
            curr_num += 1
            next_num_str = str(curr_num)
            next_length = len(next_num_str)
            # print(curr_num, next_num_str, next_length)

            if s[index:index + next_length] != next_num_str:
                beautiful = False
                break
            index += next_length
        if beautiful and index == n:
            return f'YES {first_num}'
    return "NO"


# print(is_beautiful("1234"))
# print(is_beautiful("91011"))
# print(is_beautiful("99100"))
# print(is_beautiful("101103"))
# print(is_beautiful("010203"))
print(is_beautiful("100010011002"))


def sequential(s, sub_string):
    if not s: return True
    if s.startswith(sub_string):
        l = len(sub_string)
        return sequential(s[l:], str(int(sub_string) + 1))
    return False


def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        sub_string = s[:i]
        if sequential(s, sub_string):
            return "YES " + sub_string
    return "NO"

print(separateNumbers("91011"))

def sequential_substring(s, sub_string):
    while s:
        if s.startswith(sub_string):
            l = len(sub_string)
            s = s[l:]
            sub_string = str(int(sub_string) + 1)
        else:
            return False
    return True

print(sequential_substring("9101112", '9'))

# for hacker rank only
# print No return
def sequential(s, sub_string):
    while s:
        if s.startswith(sub_string):
            l = len(sub_string)
            s = s[l:]
            sub_string = str(int(sub_string) + 1)
        else:
            return False
    return True


def separateNumbers(s):
    # Write your code here
    for i in range(1, len(s) // 2 + 1):
        sub_string = s[:i]
        if sequential(s, sub_string):
            print("YES " + sub_string)
            return
    print("NO")