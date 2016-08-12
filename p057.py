def expand(numerator, denominator):
    # Every time a / b becomes a + 2b / a + b (which in turn becomes 3a + 4b)
    return numerator + 2 * denominator, numerator + denominator

answer = 0

a, b = 3, 2

for i in range(999):
    if len(str(a)) > len(str(b)):
        answer += 1
    a, b = expand(a, b)

print(answer)
