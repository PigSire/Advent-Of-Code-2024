input = open("input.txt", "r")
#input = open("testinput.txt", "r")
direction = None
line = []
totalSafe = 0
totalIfRemoved = 0


def getDirection(line):
    if line[0] > line[1]:
        direction = "Decs"
    elif line[0] < line[1]:
        direction = "Incs"
    else:
        direction = "NoMove"
    return direction


def floorChecker(direction, line):
    for i in range(len(line) - 1):
        if direction.__eq__("Incs"):
            distance = line[i + 1] - line[i]
            if distance > 3 or distance < 1:
                safety = False
                return safety, i
        if direction.__eq__("Decs"):
            distance = line[i] - line[i + 1]
            if distance > 3 or distance < 1:
                safety = False
                return safety, i
        if direction.__eq__("NoMove"):
            safety = False
            return safety, i
    return True, 0


for i in input:
    #make a array converting all its values to ints
    line = i.split()
    line = [int(num) for num in line]
    #gets the direction
    direction = getDirection(line)
    floorSafety= floorChecker(direction, line)
    if floorSafety[0]:
        totalSafe += 1
    else:
        copy1 = line.copy()
        copy1.pop(floorSafety[1])
        copy2 = line.copy()
        copy2.pop(floorSafety[1] + 1)
        copy3 = line.copy()
        copy3.pop(floorSafety[0])
        direction = getDirection(copy1)
        copy1safety = floorChecker(direction, copy1)
        #print(str(copy1) + str(copy1safety))
        direction = getDirection(copy2)
        copy2safety = floorChecker(direction, copy2)
        direction = getDirection(copy3)
        copy3safety = floorChecker(direction, copy3)
        #print(str(copy2) + str(copy2safety))
        if copy1safety[0] or copy2safety[0] or copy3safety[0]:
            totalIfRemoved += 1
    #print(str(line) + direction + " " + str(floorSafety))
print(totalSafe)
print(totalIfRemoved)
