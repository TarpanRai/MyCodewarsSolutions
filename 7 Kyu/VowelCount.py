# Given a string, count the number of vowels

vowels = ['a', 'e', 'i', 'o', 'u']


def get_count(sentence):
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count
