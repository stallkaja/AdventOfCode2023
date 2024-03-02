import sys


def main():
    # Open file to get line count
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)

    # Open file to read lines in
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]

    cardTotal = 0
    cardSlots = [1] * linecount

    for line in lines:
        # Splitting off the card number
        splitLine = line.split(":")

        # Splitting card info to get current card number
        cardInfo = splitLine[0]
        cardInfoSplit = cardInfo.split(' ')
        cardInfoSplit = [ele for ele in cardInfoSplit if ele != '']
        cardNumber = cardInfoSplit[1]
        cardIndex = int(cardNumber) -1

        # Splitting numbers to get winners and ones I have.
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
            if (num in numsIhaveNoSpaces):
                lineCount = lineCount + 1

        for j in range(1,cardSlots[cardIndex]+1):
            for i in range(1,lineCount+1):
                cardSlots[cardIndex+i] = cardSlots[cardIndex+i] + 1

        if (lineCount != 0):
            lineTotal = (2 ** (lineCount - 1))
        else:
            lineTotal = 0
        cardTotal = cardTotal + lineTotal


    print(sum(cardSlots))


if __name__ == "__main__":
    main()
