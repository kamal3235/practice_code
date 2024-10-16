



def potion_required(k, arr):
    potion = 0
    for i in range(len(arr)):
        if i > k:
            potion += i - k
            k = i   # k is updated and keeps
            # track of the last index where the condition i > k was true.

    return potion

print(potion_required(1, [1, 2, 3, 3, 2]))