# Given a list of integers, determine whether the sum of its elements is odd or even.

def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"

