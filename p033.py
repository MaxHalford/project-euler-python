numerator = 1
denominator = 1
#don't check for numbers that include a "0"
for i in range(1, 10):
    #the first digit of the denominator has to be bigger than the first digit of the numerator
    for j in range(i+1, 10):
        for k in range(1, 10):
            #"i/k" is the stripped fraction, you compare it to the non-stripped fraction
            if i / k == int(str(i) + str(j)) /int(str(j) +str(k)):
                numerator *= i
                denominator *= k
print (denominator // numerator)
