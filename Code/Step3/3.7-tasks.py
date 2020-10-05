# n = int(input())
# def_list = [0, 0, 0, 0, 0]  # Всего игр, выигрыши(*3), проигрыши(*0), нечьи(*-1), результат
# stat = {}
# for _ in range(n):  # перебираем по одному матчу и заполняем словарь
#     line = input().split(";")
#     k1 = line[0]
#     r1 = int(line[1])
#     k2 = line[2]
#     r2 = int(line[3])
#     temp_k1 = stat.get(k1, def_list)
#     temp_k2 = stat.get(k2, def_list)
#     stat[k1] = [temp_k1[0] + 1, temp_k1[1] + 1 * (r1 > r2), temp_k1[2] + 1 * (r1 == r2), temp_k1[3] + 1 * (r1 < r2)]
#     stat[k2] = [temp_k2[0] + 1, temp_k2[1] + 1 * (r1 < r2), temp_k2[2] + 1 * (r1 == r2), temp_k2[3] + 1 * (r1 > r2)]
# for team in stat:
#     print(team, end=":")
#     print(*stat[team], end=" ")
#     print(stat[team][1] * 3 + stat[team][2] * 1 + stat[team][3] * 0)


# alphabet = input()
# codes = input()
# string_to_encode = input()
# string_to_decode = input()
#
# cypher = {}
# decypher = {}
# for i in range(len(alphabet)):  # заполняем словари шифрации и дешфирации
#     sym1 = alphabet[i]
#     sym2 = codes[i]
#     cypher[sym1] = sym2
#     decypher[sym2] = sym1
# print(str().join([cypher[sym] for sym in string_to_encode]))
# print(str().join([decypher[sym] for sym in string_to_decode]))


# dictionary = set(input().lower() for _ in range(int(input())))  # заполняем словарь
# words = set()
#
# for _ in range(int(input())):
#     for word in input().lower().split():
#         words |= {word}
# print("\n".join(words - dictionary))


# directions = {"север": [0, 1],
#               "юг": [0, -1],
#               "восток": [1, 0],
#               "запад": [-1, 0]
#               }
# position = [0, 0]
# for i in range(int(input())):
#     command = input().split()
#     position = [position[0] + directions[command[0]][0] * int(command[1]),
#                 position[1] + directions[command[0]][1] * int(command[1])]
# print(*position)

heights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
in_file = open("my_data.tsv")
for line in in_file:
    clas, height = int(line.split()[0]) - 1, int(line.split()[2])
    heights[clas] += height
    nums[clas] += 1
in_file.close()
out_file = open("class_res.txt", "w")
for i in range(11):
    print(i + 1, round(heights[i] / nums[i], 5) if heights[i] else "-", file=out_file)
out_file.close()

