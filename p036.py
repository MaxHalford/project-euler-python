def base(n, b):
    if n < b:
        return str(n)
    else:
        return base(n // b, b) + str(n % b)

# From problem 4
def palindrome(number):
    string = str(number)
    checker = True
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            checker = False
    return checker

answer = 0
for i in range(0, 10):
    for j in range(0, 10):
        # two digits palindromes
        l = int(str(i) + str(j))
        # three digits palindromes
        m = int(str(i) + str(j) + str(i))
        # four digits palindromes
        n = int(str(i) + str(j) + str(j) + str(i))
        if palindrome(l) & palindrome(int(base(l, 2))):
            answer += l
        if palindrome(m) & palindrome(int(base(m, 2))):
            answer += m
        if palindrome(n) & palindrome(int(base(n, 2))):
            answer += n
        for k in range(0, 10):
            # five digits palindromes
            m = int(str(i) + str(j) + str(k) + str(j) + str(i))
            # six digits palindromes
            n = int(str(i) + str(j) + str(k) + str(k) + str(j) + str(i))
            if palindrome(m) & palindrome(int(base(m, 2))):
                answer += m
            if palindrome(n) & palindrome(int(base(n, 2))):
                answer += n
print(answer)
