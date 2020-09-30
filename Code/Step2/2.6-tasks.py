# my_list = []
# while True:
#     my_list.append(int(input()))
#     if sum(my_list) == 0:
#         break
# new_list = [i ** 2 for i in my_list]
# print(sum(new_list))


# limit = int(input())
# n = 1
# res = []
# cnt = 0
# while cnt < limit:
#     for _ in range(n):
#         res.append(n)
#         cnt += 1
#         if cnt == limit:
#             break
#     n += 1
# print(*res)

# new_list, my_list, num = [], [int(c) for c in input().split()], int(input())
# if num not in my_list:
#     print("Отсутствует")
# else:
#     for i in range(len(my_list)):
#         if my_list[i] == num:
#             new_list.append(i)
#     print(*new_list)


# matrix = []
# while True:
#     string = input()
#     if string == "end":
#         break
#     elms = [int(item) for item in string.split()]
#     matrix.append(elms)
# rows, cols = len(matrix), len(matrix[0])
# new_matrix = []
# for i in range(rows):
#     new_row = []
#     for j in range(cols):
#         new_elm = matrix[(i - 1) % rows][j] +\
#                   matrix[(i + 1) % rows][j] + \
#                   matrix[i][(j - 1) % cols] + \
#                   matrix[i][(j + 1) % cols]
#         new_row.append(new_elm)
#     new_matrix.append(new_row)
# for i in range(rows):
#     for j in range(cols):
#         print(new_matrix[i][j], end=" ")
#     print()


# n = int(input())
# matrix = [[0]*n for i in range(n)]  # создаём матрицу заполненную нулями.
# shifts = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # приращения индексов при перемещении по матрице.
# direction = 0
# d_i, d_j = shifts[direction]
# i, j, num = 0, 0, 1
# while num <= n ** 2:
#     matrix[i][j] = num  # запись в клетку
#     num += 1  # увеличили число.
#     next_i, next_j = i + d_i, j + d_j
#     if next_i < n and next_i >= 0 and next_j < n and next_j >= 0 and matrix[next_i][next_j] == 0:  # если следующая для записи клетка не записана...
#         i, j = i + d_i, j + d_j  # изменяем индексы
#     else:
#         direction = (direction + 1) % 4  # иначе изменяем направление
#         d_i, d_j = shifts[direction]  # меняем приращения индексов
#         i, j = i + d_i, j + d_j  # и изменяем индексы
# for i in range(n):
#     print(*matrix[i])


n = int(input())
matrix = [[0]*n for i in range(n)]  # создаём матрицу заполненную нулями.
shifts = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # приращения индексов при перемещении по матрице.
direction = 0
d_i, d_j = shifts[direction]
i, j, num = 0, 0, 1
while num <= n ** 2:
    matrix[i][j] = num  # запись в клетку
    num += 1  # увеличили число.
    if matrix[(i + d_i) % n][(j + d_j) % n] != 0:  # если следующая для записи клетка занята
        direction = (direction + 1) % 4  # изменяем направление
        d_i, d_j = shifts[direction]  # меняем приращения индексов
    i, j = i + d_i, j + d_j  # и изменяем индексы
for i in range(n):
    print(*matrix[i])
