answer = 0


def digit_sum(number):
    return sum((int(s) for s in str(number)))


for a in range(100):
    for b in range(100):
        s = digit_sum(a ** b)
        if s > answer:
            answer = s

print(answer)
