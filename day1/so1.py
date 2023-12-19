import sys

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Invalid input size.\nEnter filename with extension as argument `python3 so1.py \"filename.ext\"`")
        exit()

    fileName = sys.argv[1]

    def readFirstDigit(s):
        for c in s:
            if c.isdigit():
                return int(c)
        return -1

    def readLastDigit(s):
        for c in s[::-1]:
            if c.isdigit():
                return int(c)
        return -1

    total = 0
    with open(fileName) as f:
        while line := f.readline():
            first, last = readFirstDigit(line), readLastDigit(line)
            val = first * 10 + last
            total += val
    
    print(f"Total value: {total}")