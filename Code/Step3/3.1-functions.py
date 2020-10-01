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


def my_func(name, family):
    print(f"Mister {family} has name {name}")

