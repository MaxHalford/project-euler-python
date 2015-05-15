import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#simple prime test
def primeTest(n):
    if n < 2:
        return False
    for i in range(2, int(pow(n, 1 / 2)) + 1):
        if n % i == 0:
            return False
    return True
#let's find all the primes from 2 to 1000 (b has to be prime because of when n=0)
bCandidates = [i for i in range(2, 1000) if primeTest(i)]
aCandidates = [i for i in range(-999, 1000, 1)]
#how many primes does a polynome generate?
def primeChainLength(a, b):
    n = 0
    while primeTest(n ** 2 + a * n + b) == True:
        n += 1
    return n
#now let's go through every possibility, you don't have to use a matrix if you want to go faster (but then you won't get any plot!)
M = numpy.empty([len(aCandidates), len(bCandidates)])
answer = 0
tmp = 0
for i in range(0, len(aCandidates)):
    for j in range(0, len(bCandidates)):
        a = int(aCandidates[i])
        b = int(bCandidates[j])
        M[i, j] = primeChainLength(a, b)
        if M[i, j] > tmp:
            tmp = M[i, j]
            answer = a * b
print(answer)
#let's color plot the matrix
fig, ax = plt.subplots(figsize=(6,6))
ax.imshow(M.T, cmap = cm.coolwarm, interpolation = 'nearest', origin = 'lower')
ax.set_aspect(2)
ax.set_xlabel('$a$')
ax.set_ylabel('$b$')
ax.set_title(r'Length of prime chain of $n^2+an+b$')
#plt.savefig('Problem_27.pdf', bbox_inches = 'tight')
#and display it
plt.show()
