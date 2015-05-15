import itertools
def permutations(n):
    p = list(map("".join, itertools.permutations(str(n))))
    p = [int(i) for i in p]
    return p
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(pow(n, 1 / 2)) + 1):
        if n % i == 0:
            return False
    return True
# let's list all the possibilities for which all the rotations will be checked
possibilities = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789][::-1]
answer = 0
for i in possibilities:
    for j in permutations(i):
        if prime(j):
            answer = max(answer, j)
print(answer)
