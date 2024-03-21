import sys


def main():
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    total = 0
    for line in lines:
        line = line.split(' ')
        history = []
        curLine = [eval(i) for i in line]
        history.append(curLine)
        while not all(v == 0 for v in curLine):
            nextLine = []
            for i in range(0, len(curLine) - 1):
                nextLine.append((curLine[i + 1]) - (curLine[i]))
            history.append(nextLine)
            curLine = nextLine
        historyLen = len(history) - 1
        history[historyLen] = history[historyLen] + [0]
        for i in range(0, historyLen):
            history[historyLen - i - 1] = history[historyLen - i - 1] + [
                next(reversed(history[(historyLen - i) - 1])) + next(reversed(history[historyLen - i]))]
        total += (next(reversed(history[0])))
    print("Total: " + str(total))


if __name__ == "__main__":
    main()
