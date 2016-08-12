# Function to generate primes up to n
def primes(n):
    candidates = [i for i in range(0, n+1)]
    root = int(n**0.5)
    for i in range(2, root+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2:] if i]

# Generate primes
P = primes(999999)
# Compute the cumulative sums
cumsum = P.copy()
for i in range(1, len(cumsum)):
    cumsum[i] += cumsum[i-1]
# Only keep the ones that are inferior to 1000000
candidates = [p for p in cumsum if p <= 1000000]

def main():
    # Check from highest to lowest length
    for l in range(len(candidates), 1, -1):
        # Check every sum possible of the current length
        for i in range(len(candidates) - l):
            # Calculate the difference which is a sum of primes
            difference = candidates[i+l] - candidates[i]
            # If it is a prime
            if difference in P:
                # Return and exit
                return difference

print (main())
