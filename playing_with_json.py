


import json

jsonstring = '{"name": "erik", "age": 38, "married": true}'
person = json.loads(jsonstring)
print(person['name'], 'is', person['age'], 'years old')
print(person)

person = {"name": "erik", "age": 38, "married": True}
json_string = json.dumps(person)
print(json_string)
print(type(json_string))
print(json.dumps(person, indent=1))
print(json.dumps(person, indent=2))
print(json.dumps(person, indent=4))