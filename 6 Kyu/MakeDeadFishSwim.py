#Write a simple parser that will parse and run Dead fish.

# has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.
def parse(data):
    value = 0
    output = []
    for i in data:
        if i == 'i':
            value += 1
        elif i =='d':
            value -= 1
        elif i =='s':
            value *= value
        elif i == 'o':
            output.append(value)
        else:
            continue
    return output
