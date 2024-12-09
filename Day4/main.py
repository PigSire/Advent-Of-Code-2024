#input = open("input.txt", "r")
from operator import index

input = open("testinput.txt", "r")
wordArray = []


def rotateArray(array):
    rotated = []
    for i in range(len(array)):
        stringcombined = []
        for j in range(len(array[i]), 0, -1):
            stringcombined += array[j - 1][i]
        rotated.append(stringcombined)
    return rotated

for i in input:
    splitLine = list(i)
    splitLine.pop()
    wordArray.append(splitLine)
total = 0
for i in range(4):
    wordArray = rotateArray(wordArray)
    for f in wordArray:
        print(f)
    for j in range(len(wordArray)):
        for k in range(len(wordArray[i])-3):
            position = wordArray[j][k]
            if position == "X":
                if wordArray[j][k+1] == "M":
                    if wordArray[j][k+2] == "A":
                        if wordArray[j][k + 3] == "S":
                            print("Found Xmas")
                            total += 1
    for j in range(len(wordArray)-1):
        for k in range(len(wordArray[i])-3):
            position = wordArray[j][k]
            if position == "X":
                if wordArray[j+1][k+1] == "M:":
                    if wordArray[j+2][k+2] == "A":
                        if wordArray[j+3][k + 3] == "S":
                            print("Found Xmas")
                            total += 1
print(total)


for i in range(len(wordArray)):
    for j in range(len(wordArray[i])):
        position = wordArray[i][j]
        #if position == "X":
            #print()
        #if position == "S":
            #print()