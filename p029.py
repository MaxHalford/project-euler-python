#create a set to make it easier to find duplicates
numbers = set([a ** b for a in range(2, 101) for b in range(2, 101)])
print (len(numbers))
    
