import sys


def main():
    with open('input1.txt') as f:
        linecount = sum(1 for _ in f)
    print(linecount)
    f = open("input1.txt","r")
    print(f.readline())
    f.close

if __name__ == "__main__":
    main()
