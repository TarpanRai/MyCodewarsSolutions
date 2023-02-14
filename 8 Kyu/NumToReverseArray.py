# Given a number, convert into a reversed array of digits


def digitize(n):
    output = [int(i) for i in str(n)]
    output.reverse()
    return output
