import os
os.chdir('../Project-Euler')
namesFile = open('p022_names.txt')
#then you convert the file to string
namesString = namesFile.read()
#and with the string you can build an array by spliting at the commas and striping the guillemets
names = [name.strip('"') for name in namesString.split(',')]
#then use the built-in sorting function
names.sort()
#create a dictionary giving the index of each letter
dict = {
 'A':1,
 'B':2,
 'C':3,
 'D':4,
 'E':5,
 'F':6,
 'G':7,
 'H':8,
 'I':9,
 'J':10,
 'K':11,
 'L':12,
 'M':13,
 'N':14,
 'O':15,
 'P':16,
 'Q':17,
 'R':18,
 'S':19,
 'T':20,
 'U':21,
 'V':22,
 'W':23,
 'X':24,
 'Y':25,
 'Z':26
 }
answer = 0
for i in range(0, len(names)):
    tmp = 0
    for j in range(0, len(names[i])):
        tmp += dict[names[i][j]]
    tmp *= (i + 1)
    answer += tmp
print(answer)
