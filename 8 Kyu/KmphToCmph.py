#Given a speed in km per hour, return it to cm per second


def cockroach_speed(s):
    # 1km/h -> 27.77778 cm/s
    # // 1 to get floored
    return (s * 27.77778) // 1

# or


def cockroach_speed(s):
    return s // 0.036