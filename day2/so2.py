import sys

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Invalid input size.\nEnter filename with extension as argument `python3 so2.py \"filename.ext\"`")
        exit()

    fileName = sys.argv[1]

    with open(fileName) as f:
        total = 0
        while line := f.readline():
            colorCount = {"red":0,"green":0,"blue":0}

            line = line[line.find(':')+2:] # remove Game #:

            # replace garbage characters
            chars = [',', '\n', ';']
            for c in chars:
                line = line.replace(c, ' ')
            
            # split and filter to only numbers and colors
            line = line.split(' ')
            line = list(filter(lambda x:len(x) > 0, line))

            # add to totals
            for i in range(0, len(line), 2):
                num, color = int(line[i]), line[i+1]
                colorCount[color] = max(colorCount[color], int(num))
            
            val = 1
            for color in colorCount:
                val *= colorCount[color]
            total += val
            
        print(total)
            
            