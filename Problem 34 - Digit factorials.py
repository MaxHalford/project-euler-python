def memoize(f):
   cache = {}
   def memoizedFunction(*args):
      if args not in cache:
         cache[args] = f(*args)
      return cache[args]
   memoizedFunction.cache = cache
   return memoizedFunction
@memoize
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
answer=0
def curious(n):
   n=str(n)
   sum=0
   for i in range(0,len(n)):
      sum+=factorial(int(n[i]))
   if sum==int(n):
      return True
   return False
for i in range(3,200000):
   if curious(i):
      answer+=i
print(answer)