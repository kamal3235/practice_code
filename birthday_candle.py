def tallest_candle(arr):
    if not arr:
        return 0
    tallest = arr[0]
    count = 0
    for i in range(len(arr)):
        if arr[i] > tallest:
            tallest = arr[i]
    count = arr.count(tallest)
    return count

print(tallest_candle([5, 7, 7, 3]))



def count_tallest(array):
    if not array:
        return 0
    tallest = max(array)
    count = array.count(tallest)
    return count
print(count_tallest([1, 3, 7, 7, 2, 7, 4]))




print()

