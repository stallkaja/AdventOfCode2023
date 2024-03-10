import sys
from collections import defaultdict
def main():
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])
    hands = []
    for i in range(0, len(lines)):
        hands.append(lines[i].split(' '))
    fiveOfAKind = []
    fourOfAkind = []
    fullHouse = []
    threeOfAKind = []
    twoPair = []
    onePair = []
    highCard = []
    for hand in hands:
        values = [i[0] for i in hand[0]]
        value_counts = defaultdict(lambda: 0)
        for v in values:
            value_counts[v] += 1
        if (sorted(value_counts.values()) == [5]):
            fiveOfAKind.append(hand)
        elif (sorted(value_counts.values()) == [1, 4]):
            fourOfAkind.append(hand)
        elif (sorted(value_counts.values()) == [2, 3]):
            fullHouse.append(hand)
        elif (sorted(value_counts.values()) == [1, 1, 3]):
            threeOfAKind.append(hand)
        elif (sorted(value_counts.values()) == [1, 2, 2]):
            twoPair.append(hand)
        elif (sorted(value_counts.values()) == [1, 1, 1, 2]):
            onePair.append(hand)
        elif (sorted(value_counts.values()) == [1, 1, 1, 1, 1]):
            highCard.append(hand)
        else:
            print("error")
    sortHands(fiveOfAKind)
    sortHands(fourOfAkind)
    sortHands(fullHouse)
    sortHands(threeOfAKind)
    sortHands(twoPair)
    sortHands(onePair)
    sortHands(highCard)
    combinedList = fiveOfAKind + fourOfAkind + fullHouse + threeOfAKind + twoPair + onePair + highCard
    sortedHands = list(reversed(combinedList))
    print("Sorted")
    print(sortedHands)

    total = 0
    for i in range(0,len(sortedHands)):
        total += (1+i)*int(sortedHands[i][1])
    print('Total: ' + str(total))

def sortHands(arr):
    # Traverse through 1 to len(arr)
    for i in range(0, len(arr)):
        key = arr[i][0]
        keyLocation = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and compareCards(key, arr[j][0]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = keyLocation
def compareCards(cur, next):
    Dict = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
    for i in range(0, 5):
        if (int(Dict[cur[i]]) > int(Dict[next[i]])):
            return 1
        if (int(Dict[cur[i]]) < int(Dict[next[i]])):
            return 0
    return 0

if __name__ == "__main__":
    main()
