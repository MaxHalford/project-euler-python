from math import sqrt
from itertools import permutations

# All primes up to n function
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        p = primes(int(sqrt(n)))
        no_p = [j for i in p for j in range(i*2, n, i)]
        p = [x for x in range(2, n) if x not in no_p]
    return p
# All permutations of an integer
def permute(n):
    P = [''.join(map(str, i)) for i in permutations(str(n))]
    return list(set(P))
# Get all four digit primes
candidates = [p for p in primes(10000) if p >= 1000]
# Go through each candidate
for c in candidates:
    # Generate all rotations and check if they are candidates
    perms = [int(p) for p in permute(c) if int(p) in candidates]
    # Find all sequences of 3 elements
    sequences = list(set(permutations(perms, 3)))
    # Iterate through each sequence
    for sequence in sequences:
        # Sort the sequence to compute differences
        s = sorted(sequence)
        # Check if following differences are equal
        if s[1] - s[0] == s[2] - s[1]:
            # Print the answer
            print (''.join(map(str, s)))
            break
    # Remove elements to avoid redundancy
    for p in perms:
        candidates.remove(p)
