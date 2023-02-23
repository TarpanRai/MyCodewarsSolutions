# Create a function that takes a string and return the string,
# ciphered with Rot13.



# Use maketrans() function easy
def rot13(message):
    cipherer = str.maketrans(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    )
    return message.translate(cipherer)