# Take an integer and return the digits in decending order


def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


# or


def descending_order(num):
    num = [int(d) for d in str(num)]
    num = sorted(num, reverse=True)
    num = int(''.join(map(str, num)))
    return num
