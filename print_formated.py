# Abu Kamal
# printing Given an integer
# print the following values for each integer  from  to :
# Decimal, Octal, Hexadecimal (capitalized), Binary
# values must be printed on a single line in the order specified
# Each value should be space-padded to match the width of the binary value
# values should be separated by a single space.


def print_formated(number):
    for i in range(1, number + 1):
        deci = str(i)

        octa = oct(i)[2:]

        hexa = hex(i)[2:].upper()

        bina = bin(i)[2:]

        width = len(bin(number)[2:])
        print(deci.rjust(width), octa.rjust(width), hexa.rjust(width), bina.rjust(width))


print(print_formated(20))