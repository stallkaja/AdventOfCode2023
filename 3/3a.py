import sys


def symbolCheck():
    print("checking for symbol")


def main():
    symbols = ['*', '%', '$', '#', '&', '/', '@', '+', '-']
    with open('input1.txt') as f:
        linecount = sum(1 for _ in f)
    # print(linecount)
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
                print(number)
                print(len(number))
                symbolFound = 0
                for k in range(0, len(number)):
                    print("start of num: " + str(arr[i][j - len(number)]))
                    if j-len(number)-1 >=0 and arr[i][j-len(length)-1] in symbols:
                        symbolFound = 1 # found symbol behind current
                    elif i-1>=0 and arr[i - 1][j - len(length)] in symbols:
                        #check above
                    elif():
                        #check below
                    elif():
                        #check next
                    else:
                        #?



                number = ''


if __name__ == "__main__":
    main()
