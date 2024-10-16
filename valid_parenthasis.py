


def valid_parenthesis1(s):
    map = {
        ')': '(',
        '}': "{",
        ']': '['
    }
    stack = []

    for char in s:
        if char not in map:
            stack.append(char)
            print(char)
            continue
        if not stack or stack[-1] != map[char]:
            return False
        stack.pop()

    return not stack

print(valid_parenthesis1("(){}[]"))

def valid_parenthesis_using_stack(s):
    stack = []
    for c in s:
        if c in "({[":
            stack.append(c)
        elif c == ")" and (not stack or stack.pop() != "("):
            return False
        elif c == "}" and (not stack or stack.pop() != "{"):
            return False
        elif c == "]" and (not stack or stack.pop() != "["):
            return False
    return not stack


print(valid_parenthesis_using_stack('[{()}]'))


def is_balanced(s):
    stack = []
    map = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            if not stack or stack.pop() != map[c]:
                return False

    return not stack


print(is_balanced("'[{()}]'"))