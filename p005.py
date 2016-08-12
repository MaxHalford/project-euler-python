def evenlyDivisible(number, x):                 #create a function that checks if a 'number' is evenly divisible for every integer from 1 till to x
    for i in reversed(range(1, x+1)):           #go backwards because the case happens more often(?)
        if number % i != 0:                     #evenly divisible?
            return False                        #if not then return false
    return True                                 #if so for every integer then return true
def evenlyDivisibleTo(x):                       #create a function that finds a number 'n' that would fulfill 'evenlyDivisible(n,x)'
    if x < 1:                                   #because it's recursive, consider the case 'evenlyDivisibleTo(0)
        return False                            #in that case return false (no step)
    elif x == 1:                                #because it's recursive, consider the case 'evenlyDivisibleTo(1)
        return 1                                #in that case return 1
    else:                                       #in every other case                       
        step = evenlyDivisibleTo(x-1)           #insight: divisibleto(x) = n × divisibleto(x − 1)
        number = 0                              #our number is at first 0
        found = False                           #set a boolean
        while not found:                        #continue while a valid number hasn't been found
            number += step                      #if it isn't the case increment the number to next possible candidate
            found = evenlyDivisible(number, x)  #is this new candidate valid?
        return number                           #return the first valid number
print(evenlyDivisibleTo(20))                    #give the answer for x=20



