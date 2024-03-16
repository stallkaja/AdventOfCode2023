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
    cur = {}
    for line in lines:
        if (str(line[0][len(line):-1]) == 'A'):
            cur[line[0][:-1]] = ((line[1].split(', '))[0][2:], (line[1].split(', '))[1][:-1])
        map[line[0][:-1]] = ((line[1].split(', '))[0][2:], (line[1].split(', '))[1][:-1])

    i = 0
    counts = []
    for curNode in cur:
        count = 0
        while curNode[len(curNode) - 1:] != 'Z':
            if (i >= len(instructions)):
                i = 0
            if (instructions[i] == 'L'):
                curNode = map[curNode][0]
                count+=1
            elif (instructions[i] == 'R'):
                curNode = map[curNode][1]
                count += 1
            else:
                print("error")
            i+=1
        counts.append(count)
    num1 = counts[0]
    num2 = counts[1]
    lcm = find_lcm(num1, num2)
    for i in range(2, len(counts)):
        lcm = find_lcm(lcm, counts[i])

    print("Count")
    print(lcm)


#The following code is from this source https://www.geeksforgeeks.org/lcm-of-given-array-elements/?ref=next_article
def find_lcm(num1, num2):
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm

if __name__ == "__main__":
    main()
