import sys


def main():
    f = open("input.txt","r")
    lines =(f.readlines())
    rMax = 12
    gMax = 13
    bMax = 14
    gameSum=0
    for line in lines:
        gameFlag = 1;
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
                qty = int((balls[x]))
                color = (balls[x+1])
                if(('blue' in color)and(qty > bMax)):
                    print('too many blues')
                    gameFlag =0
                elif(('red' in color)and(qty > rMax)):
                    print('too manr reds')
                    gameFlag =0
                elif(('green' in color)and(qty > gMax)):
                    print('too many green')
                    gameFlag =0
        if(gameFlag):
            gameSum = gameSum + gameNumber
    print(gameSum)
    f.close

if __name__ == "__main__":
    main()
