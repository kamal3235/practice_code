
# compare with the house limit with
# fruit tree location plus fruit fall distance

def count_apple_orange(s, t, a, b, apples, oranges):
    count_apple = 0
    count_orange = 0
    for apple in apples:
        if s <= apple + a <= t:
            count_apple += 1
    for orange in oranges:
        if orange + b >= s and orange + b <= t:
            count_orange += 1
    return count_apple, count_orange


print(count_apple_orange(2, 3, 1, 5, [-2], [-1]))
