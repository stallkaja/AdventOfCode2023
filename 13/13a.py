import sys
import math

def main():
    with open('input2.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    patterns = []
    i = 0
    j = 0
    while i < len(lines):
        if lines[i] == '':
            pattern = lines[j:i]
            patterns.append(pattern)
            j = i
            i = i + 1
        i = i + 1


    pattern = lines[j+1:i+1]
    patterns.append(pattern)
    j = 0
    for puzzle in patterns:

        # check 4 hor line
        PatLen = len(pattern)
        isOdd = PatLen % 2
        midPoint = PatLen / 2
        if isOdd:
            midPoint = math.ceil(midPoint)
        print(midPoint)
        #check before
        flag = 1
        while flag:
            #check before mid
            while i in range(0,midPoint+1):
                if
            #check after mid

        #c


if __name__ == "__main__":
    main()
