# Initialize your list and read in the value of input
# followed by  lines of commands where each command will be of the input  types
# Iterate through each command in order and perform the corresponding operation on your list.



if __name__ == '__main__':
    N = int(input())

    s = []
    for i in range(N):
        command = input().split()
        if command[0] == 'append':
            s.append(int(command[1]))
        elif command[0] == 'insert':
            s.insert(int(command[1]), int(command[2]))
        elif command[0] == 'remove':
            s.remove(int(command[1]))
        elif command[0] == 'pop':
            s.pop()
        elif command[0] == 'sort':
            s.sort()
        elif command[0] == 'reverse':
            s.reverse()
        elif command[0] == 'print':
            print(s)

# INPUT
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# OUTPUT (stdout)
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]