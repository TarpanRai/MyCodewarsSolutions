# Write a function that takes a string of parentheses,
# and determine if the order of the parentheses is valid
# Return in boolean


def valid_parentheses(string):
    count = 0
    for i in string:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False

    return count == 0
