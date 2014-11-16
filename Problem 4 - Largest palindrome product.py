def palindrome(number):                                         #create a function that checks if a number is a palindrome
    string=str(number)                                          #convert a number to a string
    checker=1                                                   #use a checker to 'check' if a property is true
    for i in range(0,len(string)//2):                           #check for i going from 0 till half of the string
        if string[i]!=string[len(string)-1-i]:                  #if a digit is different to its mirror digit
            checker=0                                           #checker is equal to 0 for 'false'
    return checker                                              #give the answer
candidates=[[0 for x in range(0,1000)] for x in range(0,1000)]  #create a list of all the possibilities
answer=0                                                        #the answer is originally 0 so we can compare later
for i in range(0,1000):                                         #go through the candidate matrix by line
    for j in range(0,1000):                                     #go through the candidate matrix by column
        candidates[i][j]=(999-i)*(999-j)                        #assign a value to the cells of the matrix
        if palindrome(candidates[i][j])==1:                     #is the value we just assigned a palindrome?
            if candidates[i][j]>answer:                         #is it higher than our current answer?
                answer=candidates[i][j]                         #if so this is the new answer
print(answer)                                                  