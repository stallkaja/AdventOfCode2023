import sys
import numpy as np
import math

def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    #print(linecount)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])

    times = lines[0].split(' ')
    times = [i for i in times if i != '']
    times.pop(0)

    distances = lines[1].split(' ')
    distances = [i for i in distances if i != '']
    distances.pop(0)
    time = ''
    distance = ''
    for x in times:
        time = time + x
    for x in distances:
        distance = distance + x
    print(time)
    print(distance)
    coeff = [-1,int(time),-1*(int(distance))]
    roots = np.roots(coeff)
    bounds = [math.ceil(min(roots)), math.floor(max(roots))]
    for j in range(0, 2):
        if (bounds[j] * (int(time) - bounds[j]) <= int(distance)):
            if (j == 0):
                bounds[j] = bounds[j] + 1
            elif (j == 1):
                bounds[j] = bounds[j] - 1
            else:
                print('error')
    print(bounds)
    numWays = bounds[1]-bounds[0]+1
    print("Numways: "+str(numWays))

if __name__ == "__main__":
    main()
