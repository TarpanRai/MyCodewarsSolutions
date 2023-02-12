# Take an integer and multiply the digits in the integer
# Keep doing it until you are left with a single digit


def persistence(n):
    # Turn integer into array or single numbers
    n = list(map(int, str(n)))
    output = 0
    while len(n) > 1:
        sum = 1
        for x in n:
            sum = sum * x
        n = list(map(int, str(sum)))
        output += 1
    return output