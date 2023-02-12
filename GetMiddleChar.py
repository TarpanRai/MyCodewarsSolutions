# Given a word, return the middle character/s of the word
# If length is even return the 2 middle characters

def get_middle(s):
    length = len(s)
    return s[(length-1)//2:(length+2)//2]
