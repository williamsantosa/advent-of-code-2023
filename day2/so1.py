import sys

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Invalid input size.\nEnter filename with extension as argument `python3 so1.py \"filename.ext\"`")
        exit()

    fileName = sys.argv[1]

    with open(fileName) as f:
        id, total = 0, 0
        while line := f.readline():
            id += 1
            validCount = {"red":12,"green":13,"blue":14}
            colorCount = {"red":0,"green":0,"blue":0}

            line = line[line.find(':')+2:] # remove Game #:

            # replace garbage characters
            chars = [',', '\n']
            for c in chars:
                line = line.replace(c, ' ')
            
            # split and filter to only numbers and colors
            line = line.split(' ')
            line = list(filter(lambda x:len(x) > 0, line))

            # add to totals
            valid = True
            for i in range(0, len(line), 2):
                num, color = int(line[i]), line[i+1]

                reset = False
                if color[-1] == ';':
                    reset = True
                    color = color[:-1]

                colorCount[color] += num

                if not all([colorCount[color] <= validCount[color] for color in colorCount.keys()]):
                    valid = False
                
                if reset:
                    for color in colorCount.keys():
                        colorCount[color] = 0

            # if valid add id
            if valid:
                total += id
            
        print(total)
            
            