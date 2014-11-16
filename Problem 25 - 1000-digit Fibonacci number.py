a,b=1,1
#the answer starts at 2 because we already have 1-1
answer=2
while len(str(b))<1000:
    a,b=b,b+a
    answer+=1
print(answer)