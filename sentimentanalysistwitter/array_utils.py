from itertools import groupby
from lambda_utils import *


def reduce_by_key(func, iterable):
    return map(
        lambda l: (l[0], reduce(func, map(get_value, l[1]))),
        groupby(sorted(iterable, key=get_key), get_key)
    )


def flat_map_double_array(iterable):
    flattened = []
    for x, y in iterable:
        for i in range(0, len(x)):
            flattened.append((x[i], y[i]))
    return flattened


def flat_map_values(iterable):
    flattened = []
    for x in iterable:
        for y in x[1]:
            flattened.append([x[0], y])
    return flattened


def join(x, y):
    dict_x = dict(x)
    dict_y = dict(y)

    common_keys = set(dict_x) & set(dict_y)
    results = map(lambda (w, z): [z, w], [[dict_x[k], dict_y[k]] for k in common_keys])
    return reduce_by_key(adder, results)


def is_not_empty(arr):
    return len(arr) > 0