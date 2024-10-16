


keys = ['Ten', 'Twemty', 'Thirty']
values = [10, 20, 30]
result = dict(zip(keys, values))
print(result)

dict1 = {'Ten': 10, 'Twenty':20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
result = {**dict1, **dict2}
print(result)

# print value of the key 'history'
sampleDict = {
    'class': {
        'student': {
            'name': 'Mike',
            'marks': {
                'physics': 70,
                'history': 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

employees = ['Kelly', 'Emma']
defaults = {'designation': 'Developer', 'Salary': 80000}
res = dict.fromkeys(employees, defaults)
print(res)

sampleDict = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'NY'
}

keys_to_remove = ['name', 'salary']
for key in keys_to_remove:
    sampleDict.pop(key, None)
print(sampleDict)

sampleDict = {'a': 100, 'b': 200, 'c': 300}
value_to_check = 200
exists = value_to_check in sampleDict.values()
print(exists)

# rename a key
sampleDict = {
    'name': 'Kelly',
    'age': 25,
    'salary': 8000,
    'city': 'NY'
}
sampleDict['location'] = sampleDict.pop('city')
print(sampleDict)

# get the key of minimum value

sampleDict = {
    'Physics': 82,
    'Math': 65,
    'History': 75
}

min_key = min(sampleDict, key=sampleDict.get)
print(min_key)

# change value of a key

sampleDict = {
    'class': {
        'student': {
            'name': 'Mike',
            'marks': {
                'physics': 70,
                'history': 80
            }
        }
    }
}

sampleDict['class']['student']['marks']['history'] = 85
print(sampleDict)

