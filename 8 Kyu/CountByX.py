# Create a function with two arguments that will return an array of the first n multiples of x.


def count_by(x, n):
    output = []
    for i in range(1, n + 1):
        output.append(x * i)
    return output




# or with list comprehension


def count_by(x, n):
    return [i * x for i in range(1, n + 1)]
