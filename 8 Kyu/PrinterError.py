# Given a string of letters. Only letter a to m are valid
# return the number of letter that are not in range of a to m



def printer_error(s):
    errors = 0
    for i in s:
        if i > 'm':
            errors += 1
    return f"{errors}/{len(s)}"