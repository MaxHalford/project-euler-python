S = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8] # One to nineteen
D = [0,3,6,6,5,5,5,7,6,6] # Ten to ninety
H = 7 # Hundred
T = 8 # Thousand
total = 0
for i in range(1,1000):
    c = i % 10 # Units digit
    b = ((i % 100) - c) // 10 # Tens digit
    a = ((i % 1000) - (b * 10) - c) // 100 # Hundreds digit
    # A hundreds digit?
    if a != 0:
        total += S[a] + H # "S[a] hundred
        if b != 0 or c != 0:
            total += 3 # "and"
    # Tens digit is 0 or 1?
    if b == 0 or b == 1:
        total += S[b * 10 + c]
    else:
        total += D[b] + S[c]
total += S[1] + T 
print (total)
