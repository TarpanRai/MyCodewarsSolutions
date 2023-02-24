# Given an array and a nth value, find the Tribonacci sequence
# until the nth value


def tribonacci(signature, n):
    # Edge case for nth value 0,1,2
    d = []
    if n == 0:
        return d
    elif n == 1 or n == 2:
        return signature[:n]
    else:
        for i in range(3, n):
            # Append the sum of the last 3 digits in the list
            signature.append(sum(signature[-3:]))
        return signature
