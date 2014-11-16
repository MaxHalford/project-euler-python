def sum_digits_fifth_powers(n):
    sum = 0
    for i in str(n):
        sum += pow(int(i),5)
    return sum
answer = 0
#loose bound: ((9**5)*n)>=(10**(n-1)-1) which gives n=6, so we get 354295=6*(9**5)
for i in range(2, 354295):
    if i == sum_digits_fifth_powers(i):
        answer += i
print(answer)