import sys


def symbolCheck():
    print("checking for symbol")


def main():
    symbols = ['*', '%', '$', '#', '&', '/', '@', '+', '-']
    total = 0
    count = 0
    with open('input1.txt') as f:
        linecount = sum(1 for _ in f)
    print(linecount)
    with open('input1.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])
    # print(linelen)
    rows, cols = (linecount, linelen)
    arr = arr = [[0] * cols] * rows
    for x in range(0, linecount):
        arr[x] = lines[x]
    print(arr)
    print("len: " + str(linelen))
    print("count: " + str(linecount))
    for i in range(0, linecount):
        number = ''
        for j in range(0, linelen):
            if str(arr[i][j]).isnumeric():
                # print(arr[i][j])
                number = number + str(arr[i][j])
                # print(number)
            elif number != '':
                #print("Current number")
                #print(number)
                #print(len(number))

                symbolFound = 0
                for k in range(0, len(number)):
                    #print("start of num: " + str(arr[i][j - len(number)]))
                    #print("cur num: " + str(arr[i][j - len(number)+k]))
                    if j-len(number)-1+k >=0 and arr[i][j-len(number)-1+k] in symbols:
                        symbolFound = 1 #found symbol behind current
                        #print("found symbol behind")
                    if i-1>=0 and arr[i - 1][j - len(number)+k] in symbols:
                        symbolFound = 1 #found symbol above current
                        #print(arr[i][j - len(number)+k])
                        #print("found symbol above")
                    if i+2<=linecount and arr[i + 1][j - len(number)+k] in symbols:
                        symbolFound = 1  # found symbol below current
                        #print(arr[i][j - len(number)+k])
                        #print("found symbol below")
                    if j-len(number)+1 <=linelen and arr[i][j - len(number)+k+1] in symbols:
                        symbolFound = 1  # found symbol to the right of current
                        #print(arr[i][j - len(number)+k])
                        #print("found symbol to the right")

                    #Diagonal Checks WIP
                    #print(k)
                    if i-1>=0 and arr[i - 1][j - len(number)+k-1] in symbols:
                        symbolFound = 1 #found symbol above current
                        #print(arr[i][j - len(number)+k])
                        print("found symbol above to the left")
                    if i+2<=linecount and arr[i + 1][j - len(number)+k-1] in symbols:
                        symbolFound = 1  # found symbol below current
                        #print(arr[i][j - len(number)+k])
                        #print("found symbol below to the left")
                    if i-1>=0 and arr[i - 1][j - len(number)+k+1] in symbols:
                        symbolFound = 1 #found symbol above current
                        #print(arr[i][j - len(number)+k])
                        #print("found symbol above to the right")
                    if i+2<=linecount and arr[i + 1][j - len(number)+k+1] in symbols:
                        symbolFound = 1  # found symbol below current
                        #print(arr[i][j - len(number)+k])
                        #print("found symbol below to the right")

                if(symbolFound):
                    print("number to add")
                    print(number)
                    total = total + int(number)
                    symbolFound = 0


                number = ''
    print("Sum")
    print(total)


if __name__ == "__main__":
    main()
