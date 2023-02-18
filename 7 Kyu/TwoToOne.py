# Given 2 strings containing only letters form a-z
# return a new sorted string of distinct letters.


# Combine both strings
# Use sets to remove duplicates
# Sort and return them to strings
def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
