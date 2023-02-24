# Write a function that checks if a given string is a palindrome
# A palindrome is a word/number/sentence that reads the same
# backward or forward

def is_palindrome(s):
    # Turn it into lowercase
    s = s.lower()
    # Check if is a palindrome
    return s == s[::-1]
