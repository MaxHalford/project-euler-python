import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#simple prime test
def prime_test(n):
    if n<2:
        return False
    for i in range(2,int(pow(n,1/2))+1):
        if n%i==0:
            return False
    return True
#let's find all the primes from 2 to 1000 (b has to be prime because of when n=0)
bCandidates=[]
for i in range(2,1000):
    if prime_test(i)==True:
        bCandidates.append(i)
#a has to be odd, because if a is even then a+1 is odd, which forces b to be even, this goes against the case when n=0
aCandidates=[]
for i in range(-999,1000,2):
    aCandidates.append(i)
#how many primes does a polynome generate?
def prime_chain_length(a,b):
    l=0
    n=0
    while prime_test(n**2+a*n+b)==True:
        n+=1
        l+=1
    return l
#now let's go through every possibility, you don't have to use a matrix if you want to go faster (but then you won't get any plot!)
M=numpy.empty([len(aCandidates),len(bCandidates)])
answer=0
tmp=0
for i in range(0,len(aCandidates)):
    for j in range(0,len(bCandidates)):
        a=int(aCandidates[i])
        b=int(bCandidates[j])
        M[i,j]=prime_chain_length(a,b)
        if M[i,j]>tmp:
            tmp=M[i,j]
            answer=a*b
#let's color plot the matrix
plt.imshow(M.T, cmap=cm.jet, interpolation='nearest',origin='lower')
#and display it
plt.show()
print(answer)