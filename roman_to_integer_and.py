



def roman_to_integer(s):
    roman_values = {
        'I': 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for char in s:
        value = roman_values[char]
        if value > prev_value:
            total += value - 2*prev_value
        else:
            total += value
        prev_value = value
    return total

print(roman_to_integer("MCMXCIV"))

def roman_to_int_forloop(s):
    values = {
        'I': 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
            total += values[s[i+1]] - values[s[i]]
            i += 2
        else:
            total += values[s[i]]
            i += 1
    return total

print(roman_to_int_forloop("MCMXCIV"))

def number_to_roman(num):
    roman_numeral = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = ""
