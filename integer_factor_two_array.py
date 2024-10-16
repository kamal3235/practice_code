


def factor_integer(a, b):
    # find integers thats are factor of element of a
    # compare b as factor to those integers

    ans = 0
    for i in range(1, 101):   # 1<a[i]<100 and 1< b[j]>100
        # check all element in a is multiple of x
        # check all element is divisible of x
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            ans += 1
    return ans

print(factor_integer([2, 6], [24, 36]))