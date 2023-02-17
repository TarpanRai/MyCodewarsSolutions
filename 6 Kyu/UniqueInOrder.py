# Given an argument, return a list of items without any
# elements with the same value to each other and preserving
# the original order of elements

def unique_in_order(sequence):
    output = []
    for i in sequence:
        if len(output) < 1 or not i == output[len(output) - 1]:
            output.append(i)
    return output
print(unique_in_order([1, 2, 2, 3, 3]))
