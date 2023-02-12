# Find the sum of the two smallest number in an array


def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    ans = numbers[0] + numbers[1]
    return ans
