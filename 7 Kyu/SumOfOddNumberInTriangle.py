# Given the triangle of consecutive odd numbers
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# Calculate the sum of the numbers in the nth row of the triangle

# The sum of the odd number is the same as the cube of the nth row
def row_sum_odd_numbers(n):
    return n ** 3
