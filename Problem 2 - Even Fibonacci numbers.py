answer, a, b = 0, 1, 2  #set the two first numbers of the sequence and the answer
while b < 4000000:      #only continue if b is inferior to 4000000
    if b%2 == 0:        #check if b is even
        answer += b     #if so then add b to answer
    a, b = b, a + b     #Fibonacci property
print(answer)

