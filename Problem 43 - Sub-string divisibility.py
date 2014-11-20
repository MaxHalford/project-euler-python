#check "Comments.pdf", the numbers are not picked at random but follow some theory
import itertools
#from Problem 41
def permutations(n):
    p=list(map("".join,itertools.permutations(str(n))))
    return p
def check(n):
    s=str(n)
    #the second triplet has to be divisible by 2 and the third triplet has to divisible by 3
    return int(s[1:4])%2==0 and int(s[2:5])%3==0    
#let's check every possibility
answer=0
for perm in permutations(4310):
    a=int(perm+'952867')
    if check(a):
        answer+=a
for perm in permutations(6410):
    a=int(perm+'357289')
    if check(a):
        answer+=a
print (answer)