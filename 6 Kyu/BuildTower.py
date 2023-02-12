# Build a pyramid-shaped tower as an array/list of string,
# given a positive integer being the number of floors
# Build the tower using '*' character

# Rule formula: 2n - 1 star
# Spaces formula: n - 1
def tower_builder(n_floors):
    spaces = n_floors - 1
    gap = ' '
    star = '*'
    output = []
    for i in range(1, n_floors + 1):
        star_num = 2 * i - 1
        shape = gap * spaces + star * star_num + gap * spaces
        spaces -= 1
        output.append(shape)
    return output
