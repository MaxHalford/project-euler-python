#find the divisors of a number
def divisors(n):
    divisors = []
    for i in range(2, int(n ** 0.5) + 1):
        q, r = divmod(n, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(n // i)
    return divisors
#check if the sum makes it abundant or not
def isAbundant(n):
    return sum(divisors(n)) + 1 > n
#find all the abundant numbers under 28124
abundants = [i for i in range(2, 28124) if isAbundant(i)]
#use a dictionnary to go faster
aNumbers = set()
#and now find all the possible sums of abundant numbers (under 28124
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        s = abundants[i] + abundants[j]
        if s <= 28123:
            aNumbers.add(s)
#now you just have to calculate the arithmetic sum of all the numbers below 28124 minus the sum of all the numbers that are sums of abundant numbers
answer = (28123 * 28124) // 2 - sum(aNumbers)
print(answer)
