#simple prime test
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(pow(n, 1 / 2))):
        if n % i == 0:
            return False
    return True
#find all the primes under 1000
primes = [i for i in range(1000) if prime(i)]
#use Fermat's little theorem
for p in primes[::-1]:
    n = 1
    # 1/p has a cycle of n digits if (10 ** n  mod p) - 1 = 0 for prime p
    while pow(10, n, p) - 1 != 0: #pow(x,y,z) is x to the power of y, and then that modulo z
        n += 1
    #a prime number in the denominator p can yield up to p − 1 repeating decimal digits (n), so when that condition is verified for p, it means it's answer
    if n == p - 1:
        break #there is no point checking for smaller primes
print (p)
