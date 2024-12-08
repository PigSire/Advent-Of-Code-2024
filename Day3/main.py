import re

input = open("input.txt", "r")
#input = open("testinput.txt", "r")
#input = open("testinputp2.txt", "r")

multipleTotal = 0
newMultipleTotal = 0
skip = False
for line in input:
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    for i in matches:
        cleanUp = i.replace("mul(", "")
        cleanUp = cleanUp.replace(")", "")
        splitNumbers = cleanUp.split(",")
        splitNumbers = [int(num) for num in splitNumbers]
        multipleTotal += splitNumbers[0]*splitNumbers[1]
    matches = re.findall(r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)', line)
    print("")
    for i in matches:
        print(str(i)+str(newMultipleTotal))
        if i == "don't()":
            skip = True
        if i == "do()":
            skip = False
        if skip == False and i != "do()":
            cleanUp = i.replace("mul(", "")
            cleanUp = cleanUp.replace(")", "")
            splitNumbers = cleanUp.split(",")
            splitNumbers = [int(num) for num in splitNumbers]
            newMultipleTotal += splitNumbers[0] * splitNumbers[1]
print(multipleTotal)
print(newMultipleTotal)