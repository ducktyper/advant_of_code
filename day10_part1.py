GRID = open("day10_input.txt").read().splitlines()
max_i = len(GRID) - 1
max_j = len(GRID[0]) - 1

start_i, start_j = None, None
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == "S":
            start_i, start_j = i, j

c_i, c_j = start_i, start_j
p_i, p_j = None, None

# first prev
if (c_j+1 <= max_j) and GRID[c_i][c_j+1] in ("-", "7", "J"):
    p_i, p_j = c_i, c_j
    c_i, c_j = c_i, c_j+1
elif (c_j-1 >= 0) and GRID[c_i][c_j-1] in ("-", "F", "L"):
    p_i, p_j = c_i, c_j
    c_i, c_j = c_i, c_j-1
elif (c_i-1 >= 0) and GRID[c_i-1][c_j] in ("|", "F", "7"):
    p_i, p_j = c_i, c_j
    c_i, c_j = c_i-1, c_j
elif (c_i+1 >= max_i) and GRID[c_i+1][c_j] in ("|", "L", "J"):
    p_i, p_j = c_i, c_j
    c_i, c_j = c_i+1, c_j
else:
    print("Error")


counter = 1
while True:
    if GRID[c_i][c_j] == "-":
        if p_i == c_i and p_j == c_j-1:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i, c_j+1
        else:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i, c_j-1
    elif GRID[c_i][c_j] == "7":
        if p_i == c_i and p_j == c_j-1:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i+1, c_j
        else:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i, c_j-1
    elif GRID[c_i][c_j] == "|":
        if p_i == c_i-1 and p_j == c_j:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i+1, c_j
        else:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i-1, c_j
    elif GRID[c_i][c_j] == "J":
        if p_i == c_i-1 and p_j == c_j:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i, c_j-1
        else:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i-1, c_j
    elif GRID[c_i][c_j] == "L":
        if p_i == c_i-1 and p_j == c_j:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i, c_j+1
        else:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i-1, c_j
    elif GRID[c_i][c_j] == "F":
        if p_i == c_i+1 and p_j == c_j:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i, c_j+1
        else:
            p_i, p_j = c_i, c_j
            c_i, c_j = c_i+1, c_j
    elif GRID[c_i][c_j] == "S":
        print(int(counter / 2))
        break
    else:
        print("ERROR")
        print(p_i, p_j, c_i, c_j)
        print(GRID[c_i-1][c_j-1], GRID[c_i-1][c_j], GRID[c_i-1][c_j+1])
        print(GRID[c_i][c_j-1], GRID[c_i][c_j], GRID[c_i][c_j+1])
        print(GRID[c_i+1][c_j-1], GRID[c_i+1][c_j], GRID[c_i+1][c_j+1])
        exit()

    counter += 1
