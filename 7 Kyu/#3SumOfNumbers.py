# Given an integer, find the next perfect square

import math


def find_next_square(sq):
    # Edge case if number is not a perfect square
    if math.sqrt(sq) % 1 != 0:
        return -1
    # Square root number, add 1 and square it
    else:
        return (math.sqrt(sq) + 1) ** 2
