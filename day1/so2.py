import sys
import re

# adapted from https://github.com/website11/My-Advent-Of-Code/blob/main/Python/2023/Day_1/Day_1.py

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Invalid input size.\nEnter filename with extension as argument `python3 so2.py \"filename.ext\"`")
        exit()

    fileName = sys.argv[1]
    
    def convert(n):
        WORDS = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                    'nine': '9'}
        return WORDS[n] if n in WORDS.keys() else str(n)
    
    def find(line):
        numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line)
        for word in numbers:
            num = convert(word)
            sub = word[0] + num + word[-1]
            line = re.sub(word, sub, line)
        numbers = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine',line)
        left, right = convert(numbers[0]), convert(numbers[-1])
        return int(left + right)

    total = 0
    with open(fileName) as f:
        while line := f.readline():
            total += find(line)
    
    print(f"Total value: {total}")