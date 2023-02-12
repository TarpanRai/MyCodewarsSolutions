# Given a string, move the first letter of each word to the
# end of it and then add 'ay' to the end of the word.

import re


def pig_it(text):
    # Split the string into an array
    text = text.split(' ')
    # Array to put transformed strings into
    output = []
    for i in text:
        # Using regrex we find if it is a special character or not, it will
        # put the first character to the end and add 'ay' to the end
        if re.match("^[a-zA-Z0-9_]*$", i):
            word = i
            pig = word[1:] + word[0] + "ay"
            output.append(pig)
        else:
            output.append(i)
    return str(output)
