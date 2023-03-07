# Write a function that removes all exclamation


def remove_exclamation_marks(s):
    return s.replace('!', '')


# or


def remove_exclamation_marks(s):
    return ''.join([i for i in s if i != '!'])
