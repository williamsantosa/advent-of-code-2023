# same as first but create a hashmap where the key is the row, column of the *
# numbers are placed after that
# obtain the sum of product where there are two adjacent numbers

import sys

# fill grid
# returns the integer value of the fill if it works
def fill(r, c, grid, hashmap):
    q = []
    q.append((r,c))
    runningTotal = 0
    stars = set()
    while q:
        x, y = q.pop(0)

        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]) or grid[x][y] == '.':
            continue
        
        elif grid[x][y].isdigit():
            runningTotal = runningTotal * 10 + int(grid[x][y])
            grid[x][y] = "."
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
                q.append((x+dx,y+dy))

        elif grid[x][y] == '*':
            stars.add((x,y))
    
    if runningTotal == 0 or len(stars) == 0:
        return

    for x, y in stars:
        key = f"{x},{y}"
        hashmap[key] = hashmap.get(key, [])
        hashmap[key].append(runningTotal)

# initial thought: similar to fill islands/number of islands problem on leetcode

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Invalid input size.\nEnter filename with extension as argument `python3 so2.py \"filename.ext\"`")
        exit()

    fileName = sys.argv[1]

    with open(fileName) as f:
        grid = []
        while line := f.readline():
            grid.append(list(line.strip()))

    hashmap = {}
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            fill(r, c, grid, hashmap)
    
    filtered = list(filter(lambda x: len(x[1]) == 2, list(hashmap.items())))
    for x, y in [p[1] for p in filtered]:
        print(x, y)
        count += x * y

    print(filtered)
    print(count)