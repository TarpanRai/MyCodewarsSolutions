# Count of distinct case-insensitive alphabetic characters
# and numeric digits that occurs more than once in the
# input string


from collections import Counter


def duplicate_count(text):
    # since it is case-insensitive, lower all characters
    text = text.lower()
    # This array will be used to separate the string into an array
    split = []
    split[:0] = text
    dup_count = 0
    # Using the dict function we will create a dictionary and the count
    dict = (Counter(split))
    for i in dict:
        if dict[i] > 1:
            dup_count += 1
    return dup_count