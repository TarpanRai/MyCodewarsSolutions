# Given a string, check if it is a pangram


def is_pangram(s):
    s = s.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in letters:
        if i not in s:
            return False
    return True
