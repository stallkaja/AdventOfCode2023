import sys


def main():
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    temp = lines[0]
    instructions = []
    lines.pop(0)  # removing instructions string from lines
    lines.pop(0)  # removing extra space from lines
    lines = [i.split('=') for i in lines]
    for ele in temp:
        instructions.append(ele)
    map = {}
    for line in lines:
        map[line[0][:-1]] = ((line[1].split(', '))[0][2:],(line[1].split(', '))[1][:-1])

    cur = 'AAA'
    count = 0
    i = 0
    while cur != 'ZZZ':
        if (i >= len(instructions)):
            i = 0
        if (instructions[i] == "L"):
            cur = map[cur][0]
            count += 1
        elif (instructions[i] == "R"):
            cur = map[cur][1]
            count += 1
        else:
            print("error")
        i += 1
    print("ZZZ has been found")
    print(count)

if __name__ == "__main__":
    main()
