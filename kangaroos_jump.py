


def kangaroos_jump(x1, v1, x2, v2):

    if x2 > x1 and v2 > v1:
        return "NO"
    else:
        if (v2 - v1) == 0:
            return "NO"
        else:
            if (x1 - x2) % (v2 - v1) == 0:
                return "YES"
            else:
                return "NO"



print(kangaroos_jump(43, 2, 70, 2))