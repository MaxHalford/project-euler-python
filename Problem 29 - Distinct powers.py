#create a set to make it easier to find duplicates
L = set() 
limit = 101 
for a in range(2,limit):
    for b in range(2,limit):
        c = a**b
        if c in L: pass
        #else
        L.add(c) 
print (len(L))
    
