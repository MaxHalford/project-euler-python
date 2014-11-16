k=600851475143                                    #set k
primeFactors=[]                                   #create a list of the prime factors of k
while k>1:                                        #if k is equal to 1, it has been divided by every prime factor of k
    i=2                                           #if you start at 1, you'll get an endless loop because 1 is always a prime factor
    while k%i!=0:                                 #if k mod i is equal 0, i is a prime factor of k
        i+=1                                      #else increment i and try again
    k=k/i                                         #reduce k once you've found a prime factor so that you can start searching the prime factors of k/i
    primeFactors.append(i)                        #add the new prime factor to the list
print(primeFactors[len(primeFactors)-1])          #print the last prime of the list