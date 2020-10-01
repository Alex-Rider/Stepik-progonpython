def f(x):
    if x <= -2:
        res = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        res = -(x / 2)
    else:
        res = (x - 2) ** 2 + 1
    return res


def modify_list(l):
    l[:] = [x // 2 for x in l if x % 2 == 0]


def update_dictionary(d, key, value):
    if key not in d.keys():
        d[key * 2] = list().append(value)
    else:
        d[key * 2].append(value)
    return d

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
