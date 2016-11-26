# Please, do not use the built-in python functions like map, reduce, len, etc.
# that solve the same problems and try to solve it yourself instead.


def map_clone(function, xs):
    return [function(x) for x in xs]

def length(xs):
    # this is a slow, naive solution
    l_size = 0
    try:
        while True:
            xs[l_size]
            l_size += 1
    except IndexError:
        return l_size


def filter_clone(function, xs):
    return [x for x in xs if function(x)]


def reverse(xs):
    if len(xs) == 0:
        return []

    wasOriginallyTuple = type(xs) == tuple

    xs = list(xs)
    for i in range(len(xs) // 2):
        xs[i], xs[len(xs) - 1 - i] = xs[len(xs) - 1 - i], xs[i]

    if wasOriginallyTuple:
        return tuple(xs)
    else:
        return xs


def append(xs, y):
    return xs + [y]


def foldl(function, xs, acc):
    for index, value in enumerate(xs):
        acc = function(acc, value)

    return acc


def foldr(function, xs, acc):
    for index, value in enumerate(reversed(xs)):
        acc = function(value, acc)

    return acc


def flat(xs):
    if xs == []:
        return []

    if type(xs[0]) == list:
        return flat(xs[0]) + flat(xs[1:])
    else:
        return [xs[0]] + flat(xs[1:])

    return xs


def concat(xs, ys):
    if ys is None:
        return xs
        
    for value in ys:
        xs.append(value)
    return xs