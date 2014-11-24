from math import sqrt
def hexagonal(n):
    return 2*n**2-n
def isPentagonal(m):
    return (1+sqrt(1+24*m))/6==int((1+sqrt(1+24*m))/6)
def isTriangular(m):
    return (sqrt(1+8*m)-1)/2==int((sqrt(1+8*m)-1)/2)
n=144
while not(isPentagonal(hexagonal(n)) and isTriangular(hexagonal(n))):
    n+=1
print(hexagonal(n))