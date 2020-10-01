def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    else:
        d[key * 2] = d.get(key * 2, []) + [value]

# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}


# text = input().lower().split()
# war_and_peace = dict()
# for word in text:
#     war_and_peace[word] = war_and_peace.get(word, 0) + 1
# for word, num in war_and_peace.items():
#     print(word, num)
# the same solution with sets
# text = input().lower().split()
# for word in set(text):
#     print(word, text.count(word))

f_res = {}
x = [int(input()) for _ in range(int(input()))]
for xi in x:
    if xi not in f_res.keys():
        f_res[xi] = f(xi)
    print(f_res[xi])
