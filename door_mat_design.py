# Abu Kamal
# Printing mat of size N and M, M = 3N
# use center function to print design in the center with fill char


N, M = map(int, input().split())

for i in range(1, N, 2): # top part
    print(('.|.'*i).center(M, '-'))
print("WELCOME".center(M, '-'))    # middle
for i in range(N-2, -1, -2):    # bottom part
    print((i*".|.").center(M, "-"))

# please enter input in the terminal to print, only N and M, M=3N