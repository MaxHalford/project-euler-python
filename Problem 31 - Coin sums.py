#dynamic programming
def ways(coins, n):
  #there is one way of making 1
  a = [1]+[0]*n
  #go through every coin in the list
  for i in coins:
    for j in range(n-i+1):
      a[i+j] += a[j]
  return a[-1]
print(ways([1,2,5,10,20,50,100,200], 200))