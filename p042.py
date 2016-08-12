import os
os.chdir("C:/Users/Max/Documents/Github/Euler-Project")
words_file = open('p042_words.txt')
# then you convert the file to string
words_string = words_file.read()
# and with the string you can build an array by spliting at the commas and striping the guillemets
words = [word.strip('"') for word in words_string.split(',')]
# then use the built-in sorting function
words.sort()
# create a dictionary giving the index of each letter
values = {
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
# find the longest word score, that should give the longest triangle number possible
maxLen = max(map(len, words)) * 26
# create a set containing triangle numbers up to maxLen
triNumbers = set([n * (n + 1) // 2 for n in range(1, maxLen)])
# define a function that gives the score of one name
def wordScore(word):
    score = 0
    for letter in word:
        score += values[str(letter)]
    return score
# go through every word and count the words whose score is a triangle number
answer = 0
for word in words:
    if wordScore(word) in triNumbers:
        answer += 1
print(answer)
