def prime(n):
    if n<2:
        return False
    for i in range(2,int(pow(n,1/2))+1):
        if n%i==0:
            return False
    return True
primes=[2]
n=3
while len(primes)<10001:
    if prime(n):
        primes.append(n)
    n+=2
print (primes[-1])