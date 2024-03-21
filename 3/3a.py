import re

def main():
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
    lines = puzzle_input.split('\n')

    regex = r'[^.\d]'
    adjacentSet = set()
    for i, line in enumerate(lines):
        for m in re.finditer(regex, line):
            j = m.start()
            adjacentSet |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}

    number_regex = r'\d+'
    part_num_sum = 0
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            if any((i, j) in adjacentSet for j in range(*m.span())):
                part_num_sum += int(m.group())

    print(part_num_sum)


if __name__ == "__main__":
    main()
