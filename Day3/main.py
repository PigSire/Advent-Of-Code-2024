import re

input = open("input.txt", "r")
#input = open("testinput.txt", "r")

multipleTotal = 0

for line in input:
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    for i in matches:
        cleanUp = i.replace("mul(","")
        cleanUp = cleanUp.replace(")","")
        splitNumbers = cleanUp.split(",")
        splitNumbers = [int(num) for num in splitNumbers]
        print(splitNumbers)
        multipleTotal += splitNumbers[0]*splitNumbers[1]
print(multipleTotal)