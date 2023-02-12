# Given an integer, get the sum of the digits in the integer
# until only a single digit is left

def digital_root(n):
    while n >= 10:
        listed = [int(i) for i in str(n)]
        n = sum(listed)
    return n
