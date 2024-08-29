import sys


def main():
    with open('input1.txt') as f:
        linecount = sum(1 for _ in f)
    # print(linecount)
    with open('input1.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])
    print(lines)
    print(linelen)
    map = []
    for line in lines:
        newLine = list(line)
        map.append(newLine)
    for y in map:
        print(y)
    print("\n")

    for i in range(0,linelen):
        for j in range(0,len(map)):

            if map[j][i] == 'O':
                k = j
                while k > 0:
                    if ((map[k - 1][i] == '.') and (map[k - 1][i] != '#')and(map[k+1][i]=='O')):
                        print("moving boulder")
                        tmp = map[k - 1][i]
                        map[k - 1][i] = '0'
                        map[k][i] = tmp
                    k = k - 1
        for y in map:
            print(y)
        print("\n")
    for y in map:
        print(y)



if __name__ == "__main__":
    main()
