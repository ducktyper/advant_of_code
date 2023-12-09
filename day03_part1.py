results = 0

NUMS = [str(x) for x in range(10)]
GRID = open("day03_input.txt").read().splitlines()

def v(i, j):
    if i < 0 or j < 0 or i >= len(GRID) or j >= len(GRID[0]):
        return False
    return GRID[i][j] not in NUMS and GRID[i][j] != '.'

for i in range(len(GRID)):
    start = False
    valid = False
    num_str = []
    for j in range(len(GRID[0])):
        if GRID[i][j] in NUMS:
            start = True
            num_str.append(GRID[i][j])
            if v(i, j) or v(i, j-1) or v(i, j+1) or v(i-1, j) or v(i-1, j-1) or v(i-1, j+1) or v(i+1, j) or v(i+1, j-1) or v(i+1, j+1):
                valid = True
        else:
            if start and valid:
                results += int("".join(num_str))
            start = False
            valid = False
            num_str = []

print(results)
