# a, b, c, d = int(input()), int(input()), int(input()), int(input())
#
# print("\t", end="")
# for col in range(c, d+1):
#     print(col, end="\t")
# print()
# for row in range(a , b+1):
#     print(row, end="\t")
#     for col in range(c, d+1):
#         print(col * row, end = "\t")
#     print()


a, b = int(input()), int(input())
n, summa = 0, 0
for x in range(a, b+1):
    if not (x % 3):
        summa += x
        n += 1
print(summa / n)