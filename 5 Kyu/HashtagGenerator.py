# Create a hashtag generator
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.


import string


def generate_hashtag(s):
    # Edge case
    if len(s) >= 140 or len(s) < 1:
        return False
    # Lower all characters
    # Capwords method to capitalize first character of each word
    s = string.capwords(s.lower())
    # Remove spaces and add # to the front
    s = s.replace(" ", "")
    return '#{}'.format(s)
