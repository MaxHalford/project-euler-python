def factor(n):
    if n in [-1, 0, 1]:
        return []
    if n < 0:
        n = -n
    F = []
    while n != 1:
        p = trialDivision(n)
        e = 1
        n /= p
        while n % p == 0:
            e += 1
            n /= p
        F.append((p, e))
    F.sort()
    return F
def trialDivision(n, bound=None):
    if n == 1:
        return 1
    for p in [2, 3, 5]:
        if n % p == 0:
            return p
    if bound == None:
        bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7
    i = 1
    while m <= bound and m * m <= n:
        if n % m == 0:
            return m
        m += dif[i % 8]
        i += 1
    return n
n = 2 * 3 * 5 * 7
chain = 1
while chain != 4:
    n += 1
    if len(factor(n)) == 4:
        chain += 1
    else:
        chain = 0
print(n - 3)
