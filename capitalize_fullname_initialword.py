
def solve(s):
    for word in s[:].split():
        print(word)
        s = s.replace(word, word.capitalize())
    return s

print(solve("abu kamal"))
