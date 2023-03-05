# Complete the solution so that the function will break up camel casing,
# using a space between words.


def solution(s):
    output = []
    for i in s:
        if i.isupper():
            output.append(" ")
            output.append(i)
        else:
            output.append(i)
    return "".join(output)



# Smarter solution than mine ;_;

def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

