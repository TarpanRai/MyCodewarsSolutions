# Given a string, replace every letter with its position
# in the alphabet

def alphabet_position(text):
    # Edge case if the text is an integer
    if text.isnumeric():
        return ''
    # remove spaces and special characters and lowercase
    rmv = ''.join(e for e in text if e.isalnum()).lower()
    print(rmv)
    output = ''
    # Using the ord function to get word unicode and -96
    # since 'a' in ascii is 97
    for i in rmv:
        asc = ord(i) - 96
        output += str(asc) + ' '
    # Remove trailing characters using rstrip()
    return output.rstrip()
