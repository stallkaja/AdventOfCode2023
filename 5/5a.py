import sys


def main():
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
    #print(maps)

    seedToSoilMap = createMap(maps,0)
    soilToFerMap = createMap(maps,1)
    ferToWaterMap = createMap(maps,2)
    waterToLightMap = createMap(maps,3)
    lightToTempMap = createMap(maps,4)
    tempToHumidMap = createMap(maps,5)
    humidToLocMap = createMap(maps,6)
    locs = []
    seeds.pop(0)

    #seed ranges
    seedRanges = []
    for i in range(0,len(seeds),2):

        seedRanges.append(range(int(seeds[i]),int(seeds[i+1])+int(seeds[i])))

    for seedRange in seedRanges:
        for seed in seedRange:
            #seeds = [int(x) for x in seedRange]
            soil = -1
            fer = -1
            water = -1
            light = -1
            temp = -1
            humid = -1
            loc = -1
            for x in seedToSoilMap:
                if(seed in x):
                    soil = seedToSoilMap[x][x.index(seed)]
            if(soil ==-1):
                soil = seed

            for x in soilToFerMap:
                if(soil in x):
                    fer = soilToFerMap[x][x.index(soil)]
            if(fer ==-1):
                fer = soil

            for x in ferToWaterMap:
                if(fer in x):
                    water = ferToWaterMap[x][x.index(fer)]
            if(water ==-1):
                water = fer

            for x in waterToLightMap:
                if(water in x):
                    light = waterToLightMap[x][x.index(water)]
            if(light ==-1):
                light = water

            for x in lightToTempMap:
                if(light in x):
                    temp = lightToTempMap[x][x.index(light)]
            if(temp ==-1):
                temp = light

            for x in tempToHumidMap:
                if(temp in x):
                    humid = tempToHumidMap[x][x.index(temp)]
            if(humid ==-1):
                humid = temp

            for x in humidToLocMap:
                if(humid in x):
                    loc = humidToLocMap[x][x.index(humid)]
            if(loc ==-1):
                loc = humid
            locs.append(loc)
    print("Lowest Location")
    print(min(locs))


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
