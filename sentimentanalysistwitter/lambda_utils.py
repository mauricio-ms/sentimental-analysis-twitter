from collections import Counter


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


def map_value_to_most_common(x):
    return get_key(x), Counter(get_value(x)).most_common()[0][0]


def multiply_word(x):
    return u"{} ".format(x[0]) * x[1]