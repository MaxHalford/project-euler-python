def criteria (a,b,c):                       #define a function that checks if a triplet meets both criterias
    if a**2+b**2==c**2 and a+b+c==1000:     #define both criterias
        return True                         #if both are met then (a,b,c) is a good candidate
    else:                                   #in the other case
        return False                        #it isn't
def searchABC():                            #now go through possibilities
    for a in range(1,501):                  #don't go beyond 500 else you'll get cases where a+b>c which isn't viable because of the first criteria
        for b in range(a,501):              #the order of (a,b,c) doesn't matter, if you start b at 1 there will redundancy
            c=1000-a-b                      #c is clearly equal to 1000-a-b
            if criteria(a,b,c)==True:       #check if a triplet meets both criterias
                return (a*b*c)              #if it does then stop and return the answer
print(searchABC())                          #give the answer

    
    

