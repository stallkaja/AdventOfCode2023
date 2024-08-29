import sys


def main():
    with open('input1.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    for i in range(0, len(lines)):
        try:
            sLoc = (i, lines[i].index("S"))
            print(sLoc)
        except ValueError:
            pass
    previousLoc = (-1,-1)
    nextLoc = ()
    curLoc = sLoc
    lOptions = ["L", "-", "F"]
    rOptions = ["J", "-", "7"]
    uOptions = ["7", "|", "F"]
    dOptions = ["J", "|", "L"]
    print(lines[2][0])
    while nextLoc != sLoc:

        for i in range(0, 4):
            try:
                # checking each direction looking for a valid connection that is not the previous location. Update next if one is found and proceed.
                match i:
                    case 0:
                        if (lines[curLoc[0] - 1][curLoc[1]] in uOptions) and ((curLoc[0] - 1, curLoc[1]) != previousLoc):  # checking up direction for valid pipe
                            print("valid pipe above")
                            nextLoc = (curLoc[0] - 1, curLoc[1])
                    case 1:
                        if (lines[curLoc[0]][curLoc[1] + 1] in rOptions) and ((curLoc[0], curLoc[1]+1) != previousLoc):  # checking right direction for valid pipe
                            print("valid pipe to the right")
                            nextLoc = (curLoc[0], curLoc[1]+1)
                    case 2:
                        if (lines[curLoc[0] + 1][curLoc[1]] in dOptions) and ((curLoc[0]+1, curLoc[1]) != previousLoc):  # checking down direction for valid pipe
                            print("valid pipe found below")
                            nextLoc = (curLoc[0]+1, curLoc[1])
                    case 3:
                        if (lines[curLoc[0]][curLoc[1] - 1] in lOptions) and ((curLoc[0], curLoc[1]-1) != previousLoc):  # checking left direction for valid pipe
                            print("valid pipe to the left")
                            nextLoc = (curLoc[0], curLoc[1]-1)
            except IndexError:
                print("checking location outside of grid")
        previousLoc = curLoc
        curLoc = nextLoc
        print("nextLoc after update")
        print(nextLoc)
        print("sLoc is")
        print(sLoc)

    # look in each direction checking if the next pipe in that direction is a valid connection
    # IE looking up the only valid choices are "| 7 F" and looking left they are "- L F"
    # need to make sure we find the "next" pipe and dont accidentally walk backwards. IE verify that previousLoc != nextLoc
    # need a try here in case you are on an edge and try to connect a pipe outside of the grid
    # continue stepping through the next pipe until you are back at sLoc
    # count steps along the way and divide by 2? or walk from both starting directions until both paths are at the same location.


if __name__ == "__main__":
    main()
