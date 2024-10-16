


def is_vowel(letter):
    return letter in 'aeiouy'

def score_words(words):
    score = 0
    for word in words:
        num_vowels = sum(1 for letter in word if is_vowel(letter))

        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1

    return score


words = ["hacker", "book", "programming", "is", "awesome"]
print(score_words(words))