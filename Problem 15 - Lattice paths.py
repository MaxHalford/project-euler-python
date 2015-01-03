def factorial(n):
     if n == 0:
         return 1
     else:
         return n * factorial(n - 1)
     
def combinations(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))

print(combinations(40, 20))
