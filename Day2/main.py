input = open("input.txt", "r")
#input = open("testinput.txt", "r")
direction = None
line = []
totalSafe = 0

def floorChecker(direction, line):
    for i in range(len(line)-1):
        if direction.__eq__("Incs"):
            distance = line[i+1] - line[i]
            if distance > 3 or distance < 1:
                floorSafety = False
                return floorSafety
        if direction.__eq__("Decs"):
            distance = line[i] - line[i+1]
            if distance > 3 or distance < 1:
                floorSafety = False
                return floorSafety
        if direction.__eq__("NoMove"):
            floorSafety = False
            return floorSafety
    return True


for i in input:
    floorSafety = True
    line = i.split()
    line = [int(num) for num in line]
    if line[0] > line[1]:
        direction = "Decs"
    elif line[0] < line[1]:
        direction = "Incs"
    else:
        direction = "NoMove"

    floorSafety = floorChecker(direction, line)
    if floorSafety:
        totalSafe += 1
    print(str(line) + direction +" "+ str(floorSafety))
print(totalSafe)