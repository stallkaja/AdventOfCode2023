import sys


def main():
    #Reading file
    with open('input.txt') as f:
        linecount = sum(1 for _ in f)
    #print(linecount)
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    linelen = len(lines[0])

    #Grabbing seeds and removing first two elements
    seeds = lines[0].split(' ')
    lines.pop(0)
    lines.pop(0)

    #Splitting the remaining lines into maps
    splitOn = ''
    maps = []
    temp_list = []
    for i in lines:
        if i == splitOn:
            temp_list.append(i)
            maps.append(temp_list)
            temp_list = []
        else:
            temp_list.append(i)
    maps.append(temp_list)

    #removing space on the end of first 6 maps, last map does not have a space at the end
    for i in range(0,6):
        maps[i].pop()

    #create maps
    seedToSoilMap = createMap(maps,0)
    soilToFerMap = createMap(maps,1)
    ferToWaterMap = createMap(maps,2)
    waterToLightMap = createMap(maps,3)
    lightToTempMap = createMap(maps,4)
    tempToHumidMap = createMap(maps,5)
    humidToLocMap = createMap(maps,6)

    #Removing the seed title and formatting strings to ints
    seeds.pop(0)
    seeds = [int(i) for i in seeds]

    locs = []
    for seed in seeds:
        soil = readMap(seedToSoilMap,seed)
        fer = readMap(soilToFerMap,soil)
        water = readMap(ferToWaterMap,fer)
        light = readMap(waterToLightMap,water)
        temp = readMap(lightToTempMap,light)
        humid = readMap(tempToHumidMap,temp)
        loc = readMap(humidToLocMap,humid)
        locs.append(loc)
    print("Lowest Location")
    print(min(locs))

def readMap(map, src):
    dest = -1
    for x in map:
        if (src in x):
            dest = map[x][x.index(src)]
    if (dest == -1):
        dest = src
    return dest

def createMap(maps,i):
    list = maps[i]
    list.pop(0)
    dict = {}
    for line in list:
        values = line.split(' ')
        destStart = int(values[0])
        srcStart = int(values[1])
        length = int(values[2])
        dict[range(srcStart, srcStart + length)] = range(destStart, destStart + length)
    return dict

if __name__ == "__main__":
    main()
