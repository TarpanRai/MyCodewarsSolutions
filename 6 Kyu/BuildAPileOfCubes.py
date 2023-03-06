# Your task is to construct a building which will be a pile of n cubes.
# The cube at the bottom will have a volume of n^3,
# the cube above will have volume of (n-1)^3 and so on until the top has a volume of 1^3
# You are given the total volume m of the building.
# Being given m can you find the number n of cubes you will have to build?


def find_nb(m):
    total = 0
    n = 0
    while total < m:
        n += 1
        total += n**3
    return n if total == m else -1





print(find_nb(6347732129459066026))


print(54532 % 1)