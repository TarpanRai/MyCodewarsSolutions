# Check if the number of 'x' is the same as number of 'o'

def xo(s):
    s = s.lower()
    if s.count('x') == s.count('o'):
        return True
    else:
        return False

