# Reverse the words in a string
def reverse_words(s):
    return ' '.join(s.split()[::-1])

# or

def reverse_words(s):
    # split the string into individual words
    words = s.split()
    # reverse the order of the words
    words.reverse()
    # join the words back together
    return ' '.join(words)
