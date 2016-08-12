for a in range(1, 501):                  #don't go beyond 500 else you'll get cases where a+b>c which isn't viable because of the first criteria
    for b in range(a, 501):              #the order of (a,b,c) doesn't matter, if you start b at 1 there will redundancy
        c = 1000 - a - b                 #c is clearly equal to 1000-a-b
        if a ** 2 + b ** 2 == c ** 2:    #check if a triplet meets both criterias
            print(a * b * c)             #if it does then stop and print the answe                

    
    

