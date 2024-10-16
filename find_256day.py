



def programmer_256th_day_of_a_year(y):
    if y == 1918:
        print('25.09.1918')
    if y < 1918:
        if y % 4 == 0:
            print('12.09.' + str(y))
        else:
            print(('13.09.' + str(y)))
    if y > 1918:
        if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
            print('12.09.' + str(y))
        else:
            print(('13.09.' + str(y)))




print(programmer_256th_day_of_a_year(1978))


def bon_appetit(bill, k, b):
    for i in range(len(bill)):
        original = sum(bill)
        Anna = original - bill[k]
    if Anna == b:
        print('Bon Appetit')
    else:
        print(Anna - b)




print(bon_appetit([3, 10, 2, 9], 1, 14))

def sock_marchant(n, arr):
    # arr1 = sorted(arr)
    # print(arr1)
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # the above code is equal to freq = Counter(arr)
    pair = 0
    for count in freq.values():
        pair += count // 2
    return pair

print(sock_marchant(20, [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]))

from collections import Counter

def count_pairs(n, ar):
    freq = Counter(ar)
    print(freq)
    pairs = 0
    for count in freq.values():
        pairs += count // 2
    return pairs


print(count_pairs(100, [44, 55, 11, 15, 4, 72, 26, 91, \
                        80, 14, 43, 78, 70, 75, 36, 83, 78, 91, \
                        17, 17, 54, 65, 60, 21, 58, 98, 87, 45, \
                        75, 97, 81, 18, 51, 43, 84, 54, 66, 10, \
                        44, 45, 23, 38, 22, 44, 65, 9, 78, 42, \
                        100, 94, 58, 5, 11, 69, 26, 20, 19, 64, \
                        64, 93, 60, 96, 10, 10, 39, 94, 15, 4, 3, \
                        10, 1, 77, 48, 74, 20, 12, 83, 97, 5, 82, \
                        43, 15, 86, 5, 35, 63, 24, 53, 27, 87, 45, \
                        38, 34, 7, 48, 24, 100, 14, 80, 54]))


