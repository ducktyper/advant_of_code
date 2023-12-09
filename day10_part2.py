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
first_move_candidates = []
if (c_j+1 <= max_j) and GRID[c_i][c_j+1] in ("-", "7", "J"):
    first_move_candidates.append((0, 1))
if (c_j-1 >= 0) and GRID[c_i][c_j-1] in ("-", "F", "L"):
    first_move_candidates.append((0, -1))
if (c_i-1 >= 0) and GRID[c_i-1][c_j] in ("|", "F", "7"):
    first_move_candidates.append((-1, 0))
if (c_i+1 >= max_i) and GRID[c_i+1][c_j] in ("|", "L", "J"):
    first_move_candidates.append((1, 0))
if len(first_move_candidates) != 2:
    print("error")
    exit()

p_i, p_j = c_i, c_j
c_i, c_j = c_i + first_move_candidates[0][0], c_j + first_move_candidates[0][1]

s_char = None
if first_move_candidates == [(0, 1), (0, -1)]:
    s_char = "-"
elif first_move_candidates == [(0, 1), (-1, 0)]:
    s_char = "L"
elif first_move_candidates == [(0, 1), (1, 0)]:
    s_char = "F"
elif first_move_candidates == [(0, -1), (-1, 0)]:
    s_char = "J"
elif first_move_candidates == [(0, -1), (1, 0)]:
    s_char = "7"
elif first_move_candidates == [(-1, 0), (1, 0)]:
    s_char = "|"
else:
    print("error")
    exit()

path = set()
path.add((p_i, p_j))

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
        # print(int(counter / 2))
        break
    else:
        print("ERROR")
        print(p_i, p_j, c_i, c_j)
        print(GRID[c_i-1][c_j-1], GRID[c_i-1][c_j], GRID[c_i-1][c_j+1])
        print(GRID[c_i][c_j-1], GRID[c_i][c_j], GRID[c_i][c_j+1])
        print(GRID[c_i+1][c_j-1], GRID[c_i+1][c_j], GRID[c_i+1][c_j+1])
        exit()

    path.add((p_i, p_j))
    counter += 1

results = 0
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if (i, j) not in path:
            counter = 0
            last = None
            for z in range(0, j):
                if (i, z) in path and GRID[i][z] not in ("-"):
                    if last == "F" and GRID[i][z] == "J":
                        pass
                    elif last == "L" and GRID[i][z] == "7":
                        pass
                    else:
                        counter += 1
                    last = GRID[i][z]
                    if last == "S":
                        last = s_char
            if counter % 2 == 1:
                results += 1

print(results)
