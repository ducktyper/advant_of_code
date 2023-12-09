INPUT = open("day13_input.txt").read().splitlines()

def solve(puzzle):
    vertical = []
    results = 0
    for i in range(len(puzzle)):
        v = []
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == "#":
                v.append("1")
            else:
                v.append("0")
        vertical.append(int("".join(v), 2))

    for i in range(len(vertical)-1):
        if vertical[i] == vertical[i+1]:
            s, f, match = i, i+1, True
            s -= 1
            f += 1
            while (s >= 0 and s < len(vertical) and f >= 0 and f < len(vertical)):
                if vertical[s] != vertical[f]:
                    match = False
                    break
                s -= 1
                f += 1
            if match:
                results += (i + 1) * 100

    holizontal = []
    for j in range(len(puzzle[0])):
        v = []
        for i in range(len(puzzle)):
            if puzzle[i][j] == "#":
                v.append("1")
            else:
                v.append("0")
        holizontal.append(int("".join(v), 2))

    for i in range(len(holizontal)-1):
        if holizontal[i] == holizontal[i+1]:
            s, f, match = i, i+1, True
            s -= 1
            f += 1
            while (s >= 0 and s < len(holizontal) and f >= 0 and f < len(holizontal)):
                if holizontal[s] != holizontal[f]:
                    match = False
                    break
                s -= 1
                f += 1
            if match:
                results += (i + 1)

    return results

puzzle = []
results = 0
for line in INPUT:
    if line == "":
        results += solve(puzzle)
        puzzle = []
    else:
        puzzle.append(line)

if len(puzzle) > 0:
    results += solve(puzzle)

print(results)
