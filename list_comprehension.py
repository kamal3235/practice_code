
# { <expression> for item in set if <conditional> }

def some_function(a):
    return (a+5) / 2
m = [some_function(x) for x in range(8)]  # range start from 0 to 7
print(m)


# nested list

x = [ [j for j in range(3)] for i in range(4)]
print(x)

y = [value for sublist in x for value in sublist]
print(y)

z = [value
     for sublist in x
     for value in sublist]
print(z)

# set comprehension
# s % 2 if it result 1, its TRUE otherwise False not included
myset = {s for s in range(1, 5) if s % 2}
print(myset)   # {1, 3}

# dict comprehension

mydict = {x: x**2 for x in (2, 4, 6)}
print(mydict)