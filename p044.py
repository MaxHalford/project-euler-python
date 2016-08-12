def answer():
    pentas = set()
    n = 0
    while True:
        n += 1
        newPenta = n * (3 * n - 1) / 2
        pentas.add(newPenta)
        for oldPenta in pentas:
            if newPenta - oldPenta in pentas and newPenta - 2 * oldPenta in pentas: 
                return newPenta - 2 * oldPenta
print(int(answer()))
