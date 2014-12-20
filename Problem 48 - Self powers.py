s=[n**n for n in range(1,1001)]
print(''.join(list(reversed(str(sum(s))[-1:-11:-1]))))
