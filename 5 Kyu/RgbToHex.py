# Given 3 values of r, g, b, convert it into hexadecimal
# Valid decimal values are from 0 - 255 (Round up to closest value)

# This function will check if the rgb values are within range
# and round them up to the closest value if they are not
def range_check(x):
    if x < 0:
        return 0
    elif x > 255:
        return 255
    else:
        return x


def rgb(r, g, b):
    return ('{:02X}' * 3).format(range_check(r), range_check(g), range_check(b))
