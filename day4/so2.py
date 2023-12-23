import sys

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Invalid input size.\nEnter filename with extension as argument `python3 so1.py \"filename.ext\"`")
        exit()

    fileName = sys.argv[1]

    count = []
    with open(fileName) as f:
        while f.readline():
            count.append(1)

    i = 0
    with open(fileName) as f:
        grid = []
        while line := f.readline():
            line = line.strip()
            line = line[line.find(':')+2:]
            nums, winners = line.split('|')
            nums, winners = nums.split(" "), winners.split(" ")
            nums, winners = set(filter(lambda x: len(x) > 0, nums)), set(filter(lambda x: len(x) > 0, winners))
            
            numWins = len(nums.intersection(winners))
            for j in range(1, numWins+1):
                if i+j >= len(count):
                    break
                count[i+j] += count[i]

            i += 1
    
    print(count)
    print(sum(count))