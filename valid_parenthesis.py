


def valid_paren(s):
    mydict = {']': '[', '}': '{', ')': '('}
    stack = []

    for char in s:
        if char in mydict:
            top_elm = stack.pop() if stack else '#'
            if mydict[char] != top_elm:
                return False
        else:
            stack.append(char)

    return not stack

print(valid_paren("()[]{}"))


def isValid(s):
    stack = []  # create an empty stack to store opening brackets
    for c in s:  # loop through each character in the string
        if c in '([{':  # if the character is an opening bracket
            stack.append(c)  # push it onto the stack
        else:  # if the character is a closing bracket
            if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                return False  # the string is not valid, so return false
            stack.pop()  # otherwise, pop the opening bracket from the stack
    return not stack  # if the stack is empty, all opening brackets have been matched
    # with their corresponding closing brackets,
    # so the string is valid, otherwise, there are
    # unmatched opening brackets, so return false

print(isValid("({[})]"))