

def print_rangoli(size):
    n = size
    import string
    design = string.ascii_lowercase
    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1] + s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1] + L))


print(print_rangoli(5))


def print_Rangoli(size):
    n = size
    l1 = list(map(chr, range(97, 123)))
    x = l1[n-1::-1] + l1[1:n]
    m = len('-'.join(x))
    for i in range(1, n):  # build logic for upper part
        print('-'.join(l1[n-1:n-i:-1] + l1[n-i:n]).center(m, '-'))
    for i in range(n, 0, -1):  # logic for lower part
        print('-'.join(l1[n-1:n-i:-1] + l1[n-i:n]).center(m, '-'))

print(print_Rangoli(6))