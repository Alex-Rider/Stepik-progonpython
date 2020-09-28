chain = input().lower()
Gs, Cs = chain.count("g"), chain.count("c")
print((Gs + Cs) / len(chain) * 100)

