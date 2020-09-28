# A, B, H = int(input()), int(input()), int(input())
# if A <= H <= B: result = "Нормально"
# elif H <= A: result = "Недосып"
# else: result = "Пересып"
# print(result)

year = int(input())
result = "Обычный"
if (year % 4 == 0) and (year % 100 != 0) or year % 400 == 0: result = "Високосный"
print(result)