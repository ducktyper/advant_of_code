NUMS = [str(x) for x in range(10)]
GRID = open("day03_input.txt").read().splitlines()

def v(i, j):
    if i < 0 or j < 0 or i >= len(GRID) or j >= len(GRID[0]):
        return False
    return GRID[i][j] not in NUMS and GRID[i][j] != '.'

data = {}
for i in range(len(GRID)):
    start = False
    sym = None
    num_str = []
    for j in range(len(GRID[0])):
        if GRID[i][j] in NUMS:
            start = True
            num_str.append(GRID[i][j])
            if v(i, j):
                sym = (i, j)
            if v(i, j-1):
                sym = (i, j-1)
            if v(i, j+1):
                sym = (i, j+1)
            if v(i-1, j):
                sym = (i-1, j)
            if v(i-1, j-1):
                sym = (i-1, j-1)
            if v(i-1, j+1):
                sym = (i-1, j+1)
            if v(i+1, j):
                sym = (i+1, j)
            if v(i+1, j-1):
                sym = (i+1, j-1)
            if v(i+1, j+1):
                sym = (i+1, j+1)
        else:
            if start and sym is not None:
                if sym not in data:
                    data[sym] = []
                data[sym].append(int("".join(num_str)))
            start = False
            sym = None
            num_str = []

results = 0
for key in data:
    if len(data[key]) > 1:
        y = 1
        for x in data[key]:
            y *= x
        results += y

print(results)
