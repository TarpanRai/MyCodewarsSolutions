# Given a string, check if the string is an Isograms or not
# Return in boolean value


# Using sets
def is_isogram(string):
    return len(string) == len(set(string.lower()))



# OR


def is_isogram(string):
    # Convert the word into lower case letters.
    string = string.lower()
    # Create a list to put already seen letters
    letters = []
    # For each loop, check if the letter has already
    # been appended to the list. Else it will append
    # it to the list
    for letter in string:
        if letter in letters:
            return False
        letters.append(letter)
    return True
