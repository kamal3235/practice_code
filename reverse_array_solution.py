# By wrapping reversed(A) with list(),
# you convert the iterator into a list.
# This is necessary if you want to work
# with the reversed sequence as a list,
# allowing you to perform list operations
# like indexing, slicing, or printing
# the entire reversed sequence at once.

def reverse_array(A):
    B = list(reversed(A))
    return B

print(reverse_array([1, 2, 3]))

def reverse_loop(arr):
    r = []
    for i in range(1, len(arr)+1):
        r.append(arr[-i])
    return r


print(reverse_loop([1, 2, 3]))

def reverse(array):
    return array[::-1]
print(reverse([1, 2, 3, 4, 5]))


def reverse_whileloop(a):
    i = len(a) - 1
    reverse_a = []
    while i >= 0:
        reverse_a.append(a[i])
        i -= 1
    return reverse_a

print(reverse_whileloop([5, 4, 3, 2, 1]))

def reverse_string(s):
    s1 = reversed(s)
    return str(s1)
print(reverse_string('abcdefgh'))

def reversed_string_slicing(s):
    return s[::-1]
print(reversed_string_slicing("hello"))