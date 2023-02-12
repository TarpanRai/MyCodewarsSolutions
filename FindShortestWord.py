# Given a string return the length of the shortest word.

def find_short(s):
    return len(min(s.split(), key=len))
