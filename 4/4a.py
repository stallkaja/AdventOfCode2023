import sys


def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    #print(linecount)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])
    cardTotal = 0
    numOfCards = []
    for line in lines:
        #Splitting off the card number
        splitLine = line.split(":")

        cardInfo = splitLine[0]
        #print(cardInfo)
        numbers = splitLine[1]

        # Splitting list of numbers into winners and nums I have
        winners = numbers.split("|")[0]
        numsIhave = numbers.split("|")[1]

        # formatting numsIhave to remove spaces and be a list of integers
        winnersNoSpaces = winners.split(" ")
        winnersNoSpaces = [ele for ele in winnersNoSpaces if ele != '']

        # formatting winners to remove spaces and be a list of integers
        numsIhaveNoSpaces = numsIhave.split(" ")
        numsIhaveNoSpaces = [ele for ele in numsIhaveNoSpaces if ele != '']

        lineCount = 0
        for num in winnersNoSpaces:
            if(num in numsIhaveNoSpaces):
                lineCount = lineCount + 1

        if(lineCount != 0):
            lineTotal = (2**(lineCount-1))
        else:
            lineTotal = 0
        cardTotal = cardTotal + lineTotal
    print(cardTotal)



if __name__ == "__main__":
    main()
