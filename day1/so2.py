import sys
import re

# adapted from https://github.com/website11/My-Advent-Of-Code/blob/main/Python/2023/Day_1/Day_1.py

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Invalid input size.\nEnter filename with extension as argument `python3 so2.py \"filename.ext\"`")
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
    
    def convert(n):
        WORDS = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                    'nine': '9'}
        return WORDS[n] if n in WORDS.keys() else str(n)
    
    def find(line):
        numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line)
        for item in numbers:
            num = convert(item)
            sub = item[0] + num + item[-1]
            line = re.sub(item, sub, line)
        numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line)
        if len(numbers) == 1:
            num = convert(numbers[0])
            return int(num + num)
        else:
            left, right = convert(numbers[0]), convert(numbers[-1])
            return int(left + right)

    total = 0
    with open(fileName) as f:
        while line := f.readline():
            total += find(line)
    
    print(f"Total value: {total}")