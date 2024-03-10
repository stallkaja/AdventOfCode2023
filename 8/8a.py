import sys


def main():
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]


    instructions = lines[0]
    lines.pop(0) #removing instructions string from lines
    lines.pop(0) #removing extra space from lines
    lines = [i.split('=') for i in lines]
    print(lines)
    print(lines[0][1].split(', '))

    #for instruction in instructions:
        #print(instruction)
    #for line in lines:
        #print(line)
    #print(lines)

    #target = 'AAA'
    #test = [item for item in lines if item[1] == target]
    #for item in lines:
        #print(item[1])
    #print(test)
    #print(sorted(lines))
    #print((sorted(lines)[0][1]).split(','))
    #print(lines)
if __name__ == "__main__":
    main()
