sequenceLength = {1: 0}
def collatzSequenceLength(n):
    #global makes it possible to use 'sequence_length' everywhere
    global sequenceLength
    #if we've already done the Collatz(n) we may as well use it again and not go through the calculations again
    if n in sequenceLength:
        return sequenceLength[n]
    #if we don't, then we'll modify our number and call our function again
    if n%2 == 0:
        length = collatzSequenceLength(n // 2)
    else:
        length = collatzSequenceLength(3*n + 1)
    length += 1
    sequenceLength[n] = length
    return length
answer = 0
currentLongest = 0
for i in range(1, 1000000):
    length = collatzSequenceLength(i)
    if length > currentLongest:
        answer = i
        currentLongest = length
print(answer)
