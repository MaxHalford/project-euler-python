#From problem 32
def isPandigital(n):
    l=len(n)
    beg=set(n[0:l])
    end=set(n[-l:])
    return beg==end and beg==set(map(str,range(1,l+1)))
answer=0
#the answer has to start with a 9, two and three digit numbers don't give enogh digits, five give too many
for n in range(9876,9213,-1):
    p=str(n*1) + str(n*2)
    if isPandigital(p): 
        answer=p
        #no point going further
        break
print(answer)