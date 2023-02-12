# Given a string, repeat the character relative to its position
# in the string
# Example: "abcd" -> "A-Bb-Ccc-Dddd"

def accum(s):
    output = []
    x = enumerate(s)
    for count, letter in x:
        output.append(letter.upper() + letter.lower() * count)
    return '-'.join(output)


print(accum("abcd"))
