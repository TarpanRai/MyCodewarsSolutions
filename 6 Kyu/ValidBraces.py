# Given a string or braces, determine if the order of the braces are valid
# Return in boolean
# Examples:
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

import re

def valid_braces(string):
    # Valid braces pairs in regrex
    valid_braces = r"\(\)|\[\]|\{\}"
    # Search for match
    while re.search(valid_braces, string):
        # If found match remove from string
        string = re.sub(valid_braces, "", string)
    # If there are no more braces, means all have pairs
    # Else false
    return len(string) == 0

