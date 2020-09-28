# sum = 0
# num = int(input())
# while num:
#     sum += num
#     num = int(input())
# print(sum)


a, b, i = int(input()), int(input()), 1
while i % a != 0 or i % b != 0:
    i += 1
print(i)


a, b, = int(input()), int(input())
i = 1
while (a * i) % b:
    i += 1
print(a * i)
