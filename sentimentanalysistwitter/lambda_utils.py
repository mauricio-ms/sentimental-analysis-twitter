def adder(x, y):
    return x + y


def concat(x, y):
    return adder(x, y)


def get_key(x):
    return x[0]


def get_value(x):
    return x[1]


def counter():
    x = 0
    return lambda y, z: x + 1
