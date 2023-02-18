
# p0 -> Starting population
# percentage -> Population growth in percentage
# aug -> New inhabitants per year
# p -> Target population
def nb_year(p0, percent, aug, p):
    # n -> Years needed to reach p
    n = 0
    current = p0
    while current < p:
        current = int(current * (percent / 100+1) + aug)
        n += 1
    return n



print(nb_year(1500, 5, 100, 5000))