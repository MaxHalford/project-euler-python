def sumDivisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum
answer = 0
for i in range(1, 10000):
    # sum of divisors of i
    x = sumDivisors(i)
    # sum of divisors of sum of divisors of i
    y = sumDivisors(x)
    # check sum of divisors of sum of divisors of i is i
    # check i isn't equal to the sum of its divisors
    if i == y and i != x:
        answer += i
print(answer)
