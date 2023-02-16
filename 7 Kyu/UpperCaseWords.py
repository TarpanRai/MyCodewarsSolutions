# Given a sentence, capatalize the starting letter in all words.

def to_jaden_case(string):
    # Edge case
    if len(string) < 1:
        return
    # Lower
    string = string.lower()
    return ' '.join(word[0].upper() + word[1:] for word in string.split(' '))


# Or use

import string


def to_jaden_case(string):
    return string.capwords()
