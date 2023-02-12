# Take a string of integer and return the highest and lowest number

def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split()]
    numbers = str(max(numbers)) + ' ' + str(min(numbers))
    return numbers
