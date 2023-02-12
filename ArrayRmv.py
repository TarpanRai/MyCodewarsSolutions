# Take an array and an integer and remove the integer from the array


def array_diff(a, b):
    result = [i for i in a if i not in b]
    return result
