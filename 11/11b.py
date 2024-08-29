import sys
import re
from itertools import combinations
from grid import Grid
def main():
    with open('input1.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])
    # print(lines)
    expandedMap = []

    # checking for empty rows
    for line in lines:
        if line.find("#") >= 0:
            expandedMap.append(line)
        elif line.find("#") == -1:
            for i in range(0,1000000):
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
                newLine = expandedMap[j][:i] + 1000000*'.' + expandedMap[j][i:]
                expandedMap[j] = newLine
    print(expandedMap)
    grid = Grid.from_text(values)
    empty_col = set(x for x in grid.x_range() if set(grid.column(x)) == {"."})
    print("Empty_Col",empty_col)
    '''
    galaxies = {}
    gCounter = 1;
    for i in range(0,len(expandedMap)):
        if expandedMap[i].find("#") >= 0:
            for j in re.finditer('#', expandedMap[i]):
                galaxies[gCounter] = (i,j.start())
                gCounter +=1

    print(galaxies)
    x = combinations([*range(1,gCounter)],2)
    gCombinations = []
    for i in x:
        gCombinations.append(i)

    print(gCombinations)

    sum = 0
    for g in gCombinations:
        print(g)
        print(g[0])
        print(galaxies[g[0]])
        print(g[1])
        print(galaxies[g[1]])
        distance = abs(galaxies[g[0]][0] - galaxies[g[1]][0]) + abs(galaxies[g[0]][1] - galaxies[g[1]][1])
        print("distance for combo",g,distance)
        sum +=distance
    print("Sum",sum)
    '''

if __name__ == "__main__":
    main()
