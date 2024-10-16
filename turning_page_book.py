



def turning_page(n, p):
    # start = 1 page =0
    # back = n
    turning_from_front = p //2
    turning_from_back = (n - p) // 2
    return min(turning_from_back, turning_from_front)

print(turning_page(5, 4))


def min_page_turns(n, p):
    # n: total number of pages in the book
    # p: target page number

    # Turns from the front
    front_turns = p // 2

    # Turns from the back
    if n % 2 == 0:
        back_turns = (n - p + 1) // 2
    else:
        back_turns = (n - p) // 2

    return min(front_turns, back_turns)

# Example usage
n = 5  # total pages
p = 4  # target page
print(min_page_turns(n, p))