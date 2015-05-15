L, tMax, pMax = 1000, 0, 0

for p in range(120, L + 1, 2):
    t = 0
    for a in range(2, p // 3):
        # expand and simplify a**2+b**2=(p-a-b)**2
        if p * (p - 2 * a) % (2 * (p - a)) == 0: 
            t += 1
            if t >= tMax:
                tMax, pMax = t, p
print(pMax)    
