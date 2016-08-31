def is_prime(n):
    if n < 2:
        return False
    for i in range(2, round(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True

k = 2 # Number of loops to the spiral
nbr_diagonal_primes = 0

while True:
    # Top right corner
    if is_prime((2 * k - 1) ** 2 - 6 * (k - 1)):
        nbr_diagonal_primes += 1
    # Top left corner
    if is_prime((2 * k - 1) ** 2 - 4 * (k - 1)):
        nbr_diagonal_primes += 1
    # Bottom left corner
    if is_prime((2 * k - 1) ** 2 - 2 * (k - 1)):
        nbr_diagonal_primes += 1

    nbr_diagonal_numbers = 4 * (k - 1) + 1

    if nbr_diagonal_primes / nbr_diagonal_numbers < 0.1:
        break

    k += 1

print(2 * k - 1)
