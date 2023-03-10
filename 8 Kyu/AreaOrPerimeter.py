# Given the length and width of a 4 sided polygon.
# If it is a square, return its area
# If it is a rectangle, return its perimeter

def area_or_perimeter(l, w):
    if l == w:
        return l * w
    else:
        return l + w + l + w