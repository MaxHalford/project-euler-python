def reverse(number):
    return int(str(number)[::-1])

def is_palindrome(number):
    string = str(number)
    if string == string[::-1]:
        return True
    return False

nbr_non_lychrel_numbers = 0

for i in range(1, 10001):
    n = i + reverse(i)
    for j in range(49):
        if is_palindrome(n):
            nbr_non_lychrel_numbers += 1
            break
        else:
            n += reverse(n)

print(10000 - nbr_non_lychrel_numbers)
