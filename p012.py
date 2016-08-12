#use the sum formula n*(n+1)/2
def numDivisors(n):
    if n % 2 == 0:
        n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors
def findTriangularIndex(factor_limit):
    n = 1
    lnum, rnum = numDivisors(n), numDivisors(n + 1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, numDivisors(n + 1)
    return n
index = findTriangularIndex(500)
triangle = (index * (index + 1)) // 2
print(triangle)
