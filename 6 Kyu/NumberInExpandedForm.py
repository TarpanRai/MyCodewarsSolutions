# Given a number, return it as a string in expanded form
# E.g. 12 -> 10 + 2
# E.g. 498 -> 400 + 90 + 8


def expanded_form(num):
    num = str(num)
    output = []
    for i, digits in enumerate(num[::-1]):
        if int(digits) != 0:
            output.append(digits + ('0' * i))
    return ' + '.join(output[::-1])
