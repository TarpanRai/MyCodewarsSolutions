# Given a string, split the string into pairs of 2 characters
# If there are odd numbers, the missing second character of the final pair
# should be paired with an underscore('_')


def solution(s):
    output = []
    # If the length is odd add a '_' to the end, making it even
    if len(s) % 2 != 0:
        s = s + "_"
    # Simple loop to append to created list
    for i in range(0, len(s), 2):
        output.append(s[i:i + 2])
    return output
