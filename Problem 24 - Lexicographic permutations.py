#we need to use combinatorics for this problem
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
#the list of digits that we will update
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#the answer will be the 1000000th
objective = 999999
#start at 9 because 10!>999999 and 9!<999999
n = 9
answer = ''
while n > 0:
    #do the euclidian division
    tmp = divmod(objective, factorial(n))
    print(tmp)
    #the next digit is the number of times 'n!' fits into 'objective'
    answer += str(digits[tmp[0]])
    #the new 'objective' becomes 'objective mod n!' 
    objective = tmp[1]
    n -= 1
    #don't use a digit twice
    digits.remove(digits[tmp[0]])
#at the end, n!>objective, so you have to add the last element in the list manually
answer += str(digits[0])
print(answer)
