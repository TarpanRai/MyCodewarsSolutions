# Given a number, return True if it is a narcissistic number
# else return false


def narcissistic(value):
    # Separate the value into digits in an array
    arr = [int(i) for i in str(value)]
    output = 0

    # Loop through the array and power it to the length of the array
    # Add each loop to a sum
    for x in range(len(arr)):
        output = output + (arr[x] ** len(arr))
    # Check the value against the sum to check if the number is a
    # narcissistic number
    if output == value:
        return True
    else:
        return False


# OR


def is_narcissistic_num(num):
    return num == sum([int(x) ** len(str(num)) for x in str(num)])
