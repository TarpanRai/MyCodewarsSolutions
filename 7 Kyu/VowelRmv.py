# Given a string, remove all vowels

def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    for i in string_:
        if i in vowels:
            string_ = string_.replace(i, '')
    return string_
