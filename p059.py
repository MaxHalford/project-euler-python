"""
Taken from https://blog.dreamshire.com/project-euler-59-solution/ because I hate
this problem.
"""
from collections import Counter

encoded_text = [int(n) for n in open('p059_cipher.txt').read().split(',')]

key = [Counter(encoded_text[i::3]).most_common(1)[0][0] ^ 32 for i in range(3)]
print('Encryption key:', ''.join(map(chr, key)))
print('Answer:', sum(x^y for x, y in zip(encoded_text, key*(len(encoded_text)//3+1))))
