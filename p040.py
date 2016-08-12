champernowne = ""
i = 1
while len(champernowne) < 1000000:
    champernowne += str(i)
    i += 1
answer = 1
for i in[1, 10, 100, 1000, 10000, 100000, 1000000]:
    answer *= int(champernowne[i - 1])
print(answer)
