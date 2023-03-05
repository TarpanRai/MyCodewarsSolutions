# Write a method that takes an array of consecutive (increasing)
# letters as input and that returns the missing letter in the array.


def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i + 1]) - ord(chars[i]) > 1:
            return chr(ord(chars[i]) + 1)
