# Given an integral number, determine if it's a square number
import math


def is_square(n):
    # Edge Case due to negative numbers
    if n < 0:
        return False
    # Find root of number and see if its whole
    n = math.sqrt(n)
    if n % 1 == 0:
        return True
    else:
        return False




