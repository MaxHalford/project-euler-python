import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def n_choose_k(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))


answer = 0


for n in range(1, 101):
    for k in range(1, n + 1):
        if n_choose_k(n, k) > 1e6:
            answer += 1

print(answer)
