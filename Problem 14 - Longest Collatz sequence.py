sequence_length = {1: 0}
def memoize(f):
   cache = {}
   def memoizedFunction(*args):
      if args not in cache:
         cache[args] = f(*args)
      return cache[args]
   memoizedFunction.cache = cache
   return memoizedFunction
@memoize
def collatz_sequence_length(n):
    #global makes it possible to use 'sequence_length' everywhere
    global sequence_length
    #if we've already done the Collatz(n) we may as well use it again and not go through the calculations again
    if n in sequence_length:
        return sequence_length[n]
    #if we don't, then we'll modify our number and call our function again
    if n%2 == 0:
        length = collatz_sequence_length(n//2)
    else:
        length = collatz_sequence_length(3*n + 1)

    length += 1
    sequence_length[n] = length
    return length
answer = 0
current_longest = 0
for i in range(1, 1000000):
    length = collatz_sequence_length(i)
    if length > current_longest:
        answer = i
        current_longest = length
print(answer)