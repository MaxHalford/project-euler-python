def prime(n):
    if n<2:
        return False
    for i in range(2,int(pow(n,1/2))+1):
        if n%i==0:
            return False
    return True
def isTrunc(n):
    for i in range(1, len(str(n))):
        if not prime(int(str(n)[i:])) or not prime(int(str(n)[:i])): 
            return False 
    return True
import re #regular expressions
n= 11
tp = []
while len(tp) < 11:
    n+=2
    if not (n > 100 and re.search('[245680]', str(n))):
        if prime(n) and isTrunc(n):
            tp.append(n)
print(sum(tp))