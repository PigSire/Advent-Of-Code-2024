#input = open("input.txt", "r")
input = open("testinput.txt","r")
leftColumn = []
rightColumn = []
totalDistance = 0

for i in input:
    splitInput = i.split()
    leftColumn.append(splitInput[0])
    rightColumn.append(splitInput[1])
leftColumn.sort(reverse=False)
rightColumn.sort(reverse=False)

for i in range(len(leftColumn)):
    totalDistance += abs(int(leftColumn[i])-int(rightColumn[i]))
    print(totalDistance)


