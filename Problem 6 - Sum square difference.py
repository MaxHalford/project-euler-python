sum_of_squares=0                            #set sum of the squares to 0
square_of_sum=0                             #set the square of the sum to 0
for i in range(1,101):                      #for i going from 1 to 100
    sum_of_squares=sum_of_squares+i**2      #add i squared to the sum of the squares
    square_of_sum=square_of_sum+i           #add i to the square of the sum
square_of_sum=square_of_sum**2              #square the square of the sum
answer=abs(sum_of_squares-square_of_sum)    #find the absolute difference (so the order doesn't matter)
print(answer)                               
