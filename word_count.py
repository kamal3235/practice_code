
# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import Counter
n = int(input())
L = {}
for i in range(n):
    value = input()
    if not L.get(value, None):
        L[value] = 1
    else:
        L[value] += 1



print(len(L))
print(*L.values())


# Input (stdin)
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Expected Output
# 3
# 2 1 1