def palindrome(n):
	s=str(n)
	if s == s[::-1]:
		return True
	return False

candidates=[[0 for x in range(0, 1000)] for x in range(0, 1000)]  #create a list of all the possibilities
answer = 0                                                        #the answer is originally 0 so we can compare later
for i in range(0, 1000):                                          #go through the candidate matrix by line
    for j in range(0, 1000):                                      #go through the candidate matrix by column
        candidates[i][j] = (999 - i) * (999 - j)                  #assign a value to the cells of the matrix
        if palindrome(candidates[i][j]):                     	  #is the value we just assigned a palindrome?
            if candidates[i][j] > answer:                         #is it higher than our current answer?
                answer = candidates[i][j]                         #if so this is the new answer
print(answer)
