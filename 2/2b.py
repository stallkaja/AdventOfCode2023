import sys


def main():
    f = open("input.txt","r")
    lines =(f.readlines())

    gameSum=0
    for line in lines:
        rMax = 0
        gMax = 0
        bMax = 0
        #print(line)
        cleanedLine = line.split(":")
        #print("cleaned line is: " + cleanedLine[1])
        gameNumberString = cleanedLine[0]
        gameNumber = int((gameNumberString[5:len(gameNumberString)]))
        print(gameNumber)
        print("---------Game number is "+str(gameNumber)+"-----------")
        #print(cleanedLine[1][:-1])
        #print(cleanedLine[len(cleanedLine)-1])
        pulls = cleanedLine[1][:-1].split(";")
        for pull in pulls:
            print("pull: "+pull)
            balls = pull.split(" ")
            balls.pop(0)
            for x in range(0,len(balls),2):
                print(bMax)
                print(rMax)
                print(gMax)
                qty = int((balls[x]))
                color = (balls[x+1])
                print(qty)
                print(color)
                if(('blue' in color)and(qty > bMax)):
                    bMax = qty
                elif(('red' in color)and(qty > rMax)):
                    rMax = qty
                elif(('green' in color)and(qty > gMax)):
                    gMax = qty
        print(bMax)
        print(rMax)
        print(gMax)
        gameNumber = bMax * rMax * gMax
        gameSum = gameSum + gameNumber
    print(gameSum)
    f.close

if __name__ == "__main__":
    main()
