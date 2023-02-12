# Convert a sting into a new string where a new character
# is '(' and ')' if the character is repeated

def duplicate_encode(word):
    # Change to lower case
    word = word.lower()
    newString = []
    for ch in word:
        if word.count(ch) == 1:
            newString.append('(')
        else:
            newString.append(')')
    return ''.join(newString)
