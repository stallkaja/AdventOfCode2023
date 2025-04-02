import sys


def main():
    f = open("input.txt","r")
    lines = f.readlines()
    sum =0
    for line in lines:
        length = len(line)-1
        first = length
        last = 0
        a = x
        index = 0
        digits = ['one','two','three','four','five','six','seven','eight','nine']
        word2Num = {'one':1,
                    'two':2,
                    'three':3,
                    'four':4,
                    'five':5,
                    'six':6,
                    'seven':7,
                    'eight':8,
                    'nine':9
                    }
        useWord = 1
        #print(line)
        for digit in digits:
            index = line.find(digit)
            if(index<first and index!=-1):
                #print("found word form, updating first")
                first = index
                wordFound = digit
        for x in range(length):
            if(line[x].isnumeric()and x<first):
                #print("found number earlier than word, updating to number")
                first = x
                useWord = 0

        if(useWord):
            firstNumber = word2Num.get(wordFound)
        else:
            firstNumber = line[first]
        #print(firstNumber)

        useWord = 1
        last = -1
        for digit in digits:
            index = line.rfind(digit)
            if(index>last and index!=-1):
                #print("found word form, updating first")
                last = index
                wordFound = digit
        for x in range(length+1):
            print("last: " +str(last))
            print("x: "+str(x))
            print("curr num: "+line[length-x])
            if(line[length-x].isnumeric()and ((length-x)>last)):
                last = length-x
                useWord = 0
        if(useWord):
            lastNumber = word2Num.get(wordFound)
        else:
            lastNumber = line[last]


        print(line)
        print("first "+str(firstNumber))
        print("last "+str(lastNumber))
        number = str(firstNumber) + str(lastNumber)
        print("number: " + number)
        sum = sum + int(number)
        print("--------------")
    print(sum)
    f.close

if __name__ == "__main__":
    main()
