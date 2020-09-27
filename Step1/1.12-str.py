# a, b, c = int(input()), int(input()), int(input())
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(S)

# a = int(input())
# print((-15 < a <=12) or (14 < a < 17) or (19 <= a))

# Simple calc.
a, b, oper = float(input()), float(input()), input()
if oper == "+": res = a + b
elif oper == "-": res = a - b
elif oper == "*": res = a * b
elif oper == "pow": res = a ** b
elif b == 0: res = "Деление на 0!"
elif oper == "/": res = a / b
elif oper == "mod": res = a % b
elif oper == "div": res = a // b
else: res = "Ошибка операции!"
print(res)