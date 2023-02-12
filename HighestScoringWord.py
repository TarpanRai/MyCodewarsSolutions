# Given a string of words, find the highest scoring word
# Each word scores points according to its position in the alphabet
# Example: a=1, b=2, c=3
# If two words score the same, return the word that appears the earliest

def high(x):
    # Separate the string into a list of words
    x = list(x.split(' '))
    # We will use this list to put the sum of the word in order
    word_list = []
    # Using the ord function to get word unicode and -96
    # since 'a' in ascii is 97
    for z in x:
        word_list.append(sum([ord(i) - 96 for i in z]))
    # Get the highest number in the list since we need the biggest
    highest_num = max(word_list)
    # Get the index of the highest number in a list
    idx = word_list.index(highest_num)
    # Use the index to get the corresponding index and turn it to string
    output = str(x[idx])
    return output


print(high('man i need a taxi up to ubud'))