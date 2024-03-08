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

    boundaries = []
    for i in range(0,len(times)):
        coeff = [-1, int(times[i]), (-1 * int(distances[i]))]
        #print(coeff)
        roots = np.roots(coeff)
        bounds = [math.ceil(min(roots)),math.floor(max(roots))]
        for j in range(0,2):
            if(bounds[j] *(int(times[i])-bounds[j])<=int(distances[i])):
                if(j==0):
                    bounds[j] = bounds[j] +1
                elif(j==1):
                    bounds[j] = bounds[j]-1
                else:
                    print('error')
        boundaries.append(bounds)
    total = 1
    for set in boundaries:
        numWays = set[1]-set[0]+1
        total = total * numWays
    print("Margin of error: " + str(total))


if __name__ == "__main__":
    main()
