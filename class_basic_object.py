# simple class
# how iter and next works



class EvenNumbers:
    current = 0

    def __iter__(self):
        return self
    def __next__(self):
        self.current += 2

        if self.current > 8:
            raise StopIteration
        return self.current

even_numbers = EvenNumbers()
for num in even_numbers:
    print(num)
print()
print([x for x in range(1, 5)])
print(list(range(1, 5)))

