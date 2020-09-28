# chain = input().lower()
# Gs, Cs = chain.count("g"), chain.count("c")
# print((Gs + Cs) / len(chain) * 100)


chain = input().lower()
res = chain[0]
cnt = 0
for sym in chain:
    if sym == res[-1]:
        cnt += 1
    else:
        res += str(cnt)
        res += sym
        cnt = 1
print(res)