# Function to generate primes up to n
def primes(n):
    candidates = [i for i in range(0, n+1)]
    root = int(n**0.5)
    for i in range(2, root+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2:] if i]
