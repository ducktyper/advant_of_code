GRID = open("day11_input.txt").read().splitlines()

galaxies = []
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == "#":
            galaxies.append((i, j))

i_expand = set()
for i in range(len(GRID)):
    empty = True
    for j in range(len(GRID[0])):
        if GRID[i][j] == "#":
            empty = False
    if empty:
        i_expand.add(i)

j_expand = set()
for j in range(len(GRID[0])):
    empty = True
    for i in range(len(GRID)):
        if GRID[i][j] == "#":
            empty = False
    if empty:
        j_expand.add(j)

results = 0
for i in range(len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        results += abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])

        if galaxies[i][0] < galaxies[j][0]:
            for x in range(galaxies[i][0], galaxies[j][0] + 1):
                if x in i_expand:
                    results += 1
        else:
            for x in range(galaxies[j][0], galaxies[i][0] + 1):
                if x in i_expand:
                    results += 1

        if galaxies[i][1] < galaxies[j][1]:
            for x in range(galaxies[i][1], galaxies[j][1] + 1):
                if x in j_expand:
                    results += 1
        else:
            for x in range(galaxies[j][1], galaxies[i][1] + 1):
                if x in j_expand:
                    results += 1

print(results)
