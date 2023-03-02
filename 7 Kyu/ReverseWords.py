# Reverses each word in the string.
# All spaces in the string should be retained.

def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(" "))

