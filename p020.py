def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
strNumber = str(factorial(100))
answer = 0
for i in range(0, len(strNumber)):
    answer += int(strNumber[i])
print(answer)
