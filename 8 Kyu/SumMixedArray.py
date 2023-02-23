# Given an array of integers as strings and numbers,
# return the sum of the array values as if all were numbers.

def sum_mix(arr):
    return sum(list(map(int, arr)))
