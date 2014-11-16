sieve = [True] * 2000000                                    #create a list of 2M of numbers which are at first all 'true' (prime)
def mark(sieve, x):                                         #if x is prime, then k*x isn't prime, is has to be marked 'false'
    for i in range(x+x, len(sieve), x):                     #linear step
        sieve[i] = False                                    #'false' means the number is composite
for x in range(2, int(len(sieve) ** 0.5) + 1):              #going through 2 to sqrt(n) is only required
    if sieve[x]==True:                                      #checks for the next prime number
        mark(sieve, x)                                      #and then goes through all its multiples
print (sum(i for i in range(2, len(sieve)) if sieve[i]))    #print the sum of the list