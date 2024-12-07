#input = open("input.txt", "r")
input = open("testinput.txt", "r")
direction = None
line = []
for i in input:
    line = i.split()
    if line[0] > line[1]:
        direction = "Decs"
    elif line[0] < line[1]:
        direction = "Incs"
    else:
        direction = "NoMove"
    print(str(line) + direction)