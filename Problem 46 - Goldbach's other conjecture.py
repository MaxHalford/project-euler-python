n=5
primes=set()
while True:
    #If n is prime
    if all(n%p for p in primes):
        primes.add(n)
    #If n is composite
    else:
        #Check if n minus any square is any prime is false
        if not any((n-2*s**2) in primes for s in range(1,int(n**1/2))):
            break
    #Get the next odd number
    n+=2
print(n)