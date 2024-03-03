import sys


def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    #print(linecount)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])
    print(lines)

if __name__ == "__main__":
    main()
