import math


def zero_vector(vector):
    for i in vector:
        if i != 0:
            return False
    return True


def myround(x):
    decimal, integer = math.modf(x)
    if decimal >= 0.5:
        return integer + 1
    return integer
