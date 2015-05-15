# For how many digits does the property hold?
n = 1
while n * 9 ** 5 > 10 ** n:
    n += 1
sumDigitsFifthPower = lambda n: sum((pow(int(i), 5) for i in str(n)))
# loose bound: n*9**5 < 10**n which gives n=6, so we get 354295=6*(9**5)
answer = sum((n for n in range(2, n * 9 ** 5) if n == sumDigitsFifthPower(n)))
print(answer)




