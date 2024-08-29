import sys
import re
from itertools import combinations
def main():
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])
    # print(lines)
    expandedMap = []

    # checking for empty rows
    for line in lines:
        if line.find("#") >= 0:
            expandedMap.append(line)
        elif line.find("#") == -1:
            expandedMap.append(line)
            expandedMap.append(line)

    linecount = len(expandedMap)
    # checking for empty columns
    flag = 0
    for i in range(0, linelen + 1):
        column = [row[i] for row in expandedMap]
        if (flag == 1):
            flag = 0
            continue
        if ('#' not in column):
            flag = 1
            for j in range(0, linecount):
                newLine = expandedMap[j][:i] + '.' + expandedMap[j][i:]
                expandedMap[j] = newLine
    galaxies = {}
    gCounter = 1;
    for i in range(0,len(expandedMap)):
        if expandedMap[i].find("#") >= 0:
            for j in re.finditer('#', expandedMap[i]):
                galaxies[gCounter] = (i,j.start())
                gCounter +=1

    x = combinations([*range(1,gCounter)],2)
    gCombinations = []
    for i in x:
        gCombinations.append(i)


    sum = 0
    for g in gCombinations:
        distance = abs(galaxies[g[0]][0] - galaxies[g[1]][0]) + abs(galaxies[g[0]][1] - galaxies[g[1]][1])
        sum +=distance
    print("Sum",sum)


if __name__ == "__main__":
    main()
