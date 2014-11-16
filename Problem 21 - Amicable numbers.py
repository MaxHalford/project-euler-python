def d(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum
answer=0
for i in range(1,10000):
    x=d(i)
    y=d(x)
    if i==y and i!=x:
        answer+=i
print (answer)