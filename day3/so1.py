import sys

# fill grid
# returns the integer value of the fill if it works
def fill(r, c, grid):
    q = []
    q.append((r,c))
    runningTotal = 0
    valid = False
    while q:
        x, y = q.pop(0)

        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]) or grid[x][y] == '.':
            continue
        
        elif not grid[x][y].isdigit():
            valid = True

        else:
            runningTotal = runningTotal * 10 + int(grid[x][y])
            grid[x][y] = "."
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
                q.append((x+dx,y+dy))
    
    if runningTotal == 0:
        pass
    elif valid:
        print(runningTotal, "\n-------------------------------------\n")
    elif not valid:
        print(runningTotal, "\n----^invalid-------------------------\n")
    return runningTotal if valid else 0


# initial thought: similar to fill islands/number of islands problem on leetcode

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Invalid input size.\nEnter filename with extension as argument `python3 so1.py \"filename.ext\"`")
        exit()

    fileName = sys.argv[1]

    with open(fileName) as f:
        grid = []
        while line := f.readline():
            grid.append(list(line.strip()))
            
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            count += fill(r, c, grid)
    
    print(count)