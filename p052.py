def sort_digits(n):
    return sorted(str(n))

n = 1

while True:
    digits = sort_digits(n)
    has_same_digits = True

    for i in range(2, 7):
        if sort_digits(i * n) != digits:
            has_same_digits = False
            break

    if has_same_digits:
        break

    n += 1

print(n)
