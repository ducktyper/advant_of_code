INPUT = open("day14_input.txt").read().splitlines()

results = 0
for j in range(len(INPUT[0])):
    si = -1
    diff = 0
    for i in range(len(INPUT)):
        if INPUT[i][j] == "#":
            si = i
            diff = 0
        elif INPUT[i][j] == "O":
            results += len(INPUT) - (si + 1 + diff)
            diff += 1

print(results)

