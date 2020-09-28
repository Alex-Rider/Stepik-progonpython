# a, b, c = int(input()), int(input()), int(input())
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(S)

# a = int(input())
# print((-15 < a <=12) or (14 < a < 17) or (19 <= a))


# # Simple calc.
# a, b, oper = float(input()), float(input()), input()
# if oper == "+": res = a + b
# elif oper == "-": res = a - b
# elif oper == "*": res = a * b
# elif oper == "pow": res = a ** b
# elif b == 0: res = "Деление на 0!"
# elif oper == "/": res = a / b
# elif oper == "mod": res = a % b
# elif oper == "div": res = a // b
# else: res = "Ошибка операции!"
# print(res)


# figure = input()
# if figure == "треугольник":
#     a, b, c = int(input()), int(input()), int(input())
#     p = (a + b + c) / 2
#     S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# elif figure == "прямоугольник":
#     a, b = int(input()), int(input())
#     S = a * b
# elif figure == "круг":
#     r = int(input())
#     pi = 3.14
#     S = pi * r ** 2
# print(float(S))


# a, b, c = int(input()), int(input()), int(input())
# if a >= b >= c:
#     max, mid, min = a, b, c
# elif a >= c >= b:
#     max, mid, min = a, c, b
# elif b >= a >= c:
#     max, mid, min = b, a, c
# elif b >= c >= a:
#     max, mid, min = b, c, a
# elif c >= a >= b:
#     max, mid, min = c, a, b
# else:
#     max, mid, min = c, b, a
# print(max, min, mid, sep="\n")



# num = input()
# root = "программист"
# ends = ("ов", "", "а", "а", "а", "ов", "ов", "ов", "ов", "ов")
# if len(num) == 1:
#     end = ends[int(num)]
# else:
#     if 10 < int(num[-2:]) < 19:
#         end = "ов"
#     else:
#         end = ends[int(num[-1])]
# print(num, root + end)



number = input()
if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]): print("Счастливый")
else: print("Обычный")
