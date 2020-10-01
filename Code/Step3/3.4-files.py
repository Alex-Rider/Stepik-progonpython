# with open('dataset.txt') as in_file:
#     lines = in_file.readlines()
# out_file = open("result.txt", "w")
# for line in lines:
#     i = 0
#     while i < len(line) - 1:
#         sym = line[i]
#         num = ""
#         j = i + 1
#         while j < len(line) and line[j].isnumeric():
#             j += 1
#         print(sym * int(line[i + 1:j]), end="", file=out_file)
#         i = j
# out_file.close()


# words = {}
# with open('mytext.txt') as in_file:
#     for line in in_file:
#         line = line.lower().strip()
#         for word in line.split():
#             words[word] = words.get(word, 0) + 1
#
# out_file = open("words_res.txt", "w")
# for word in sorted(words, key=words.get, reverse=True):
#     print(f"{word} : {words[word]}", file=out_file)
# out_file.close()

math = []
phys = []
russ = []
data_file = open("pupils.txt", "r", encoding="utf-8")
res_file = open("pupils_res.txt", "w")
for line in data_file:
    raw = line.strip().split(";")
    name, o_math, o_phys, o_russ = raw[0], int(raw[1]), int(raw[2]), int(raw[3])
    avg = round((o_math + o_phys + o_russ) / 3, 9)
    math.append(o_math)
    phys.append(o_phys)
    russ.append(o_russ)
    print(f"Name: {name}, math={o_math}, phys={o_phys}, russ={o_russ}, avg={avg}")
    print(avg, file=res_file)
print(sum(math) / len(math), sum(phys) / len(phys), sum(russ) / len(russ), file=res_file)