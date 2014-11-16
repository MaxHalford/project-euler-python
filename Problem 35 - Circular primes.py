def primeTest(n):
    if n<2:
        return False
    for i in range(2,int(pow(n,1/2))+1):
        if n%i==0:
            return False
    return True
def rotate(n):
    #transform the number into a list
    l=str(n)
    #create a matrix of strings containing all the rotations of 'l'
    m=[l[i:] + l[:i] for i in range(0, len(l))]
    #now transform the strings into integers
    for i in range(len(m)):
        tmp=""
        for j in range(len(m[i])):
            tmp+=m[i][j]
        m[i]=int(tmp)
    #return the list of rotations
    return m
def circularPrime(n):
    rotations=rotate(n)
    #check if all the rotations are prime
    for i in rotations:
        if primeTest(i)==False:
            return False
    return True
#don't forget to count 2!
answer=1
digits=["0","1","3","5","7","9"]
for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:
                for m in digits:
                    for n in digits[1:]:
                        if circularPrime(int(i+j+k+l+m+n)):
                            answer+=1
print(answer)