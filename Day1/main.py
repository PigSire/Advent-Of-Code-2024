input = open("input.txt", "r")
#input = open("testinput.txt","r")
leftColumn = []
rightColumn = []
totalDistance = 0
similarityScore = 0

for i in input:
    splitInput = i.split()
    leftColumn.append(int(splitInput[0]))
    rightColumn.append(int(splitInput[1]))
leftColumn.sort(reverse=False)
rightColumn.sort(reverse=False)

for i in range(len(leftColumn)):
    totalDistance += abs(leftColumn[i]-rightColumn[i])
print(totalDistance)

for i in range(len(leftColumn)):
    timesFound = rightColumn.count(leftColumn[i])
    similarityScore += leftColumn[i] * timesFound
print(similarityScore)


