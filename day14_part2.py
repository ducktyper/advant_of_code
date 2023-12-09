DATA = open("day14_input.txt").read().splitlines()
INPUT = []

for row in DATA:
    INPUT.append([x for x in row])
# for row in INPUT:
#     print(row)

candidates = []
for _ in range(100):
    for j in range(len(INPUT[0])):
        si = -1
        diff = 0
        for i in range(len(INPUT)):
            if INPUT[i][j] == "#":
                for x in range(si+1, si+1+diff):
                    INPUT[x][j] = "O"
                si = i
                diff = 0
            elif INPUT[i][j] == "O":
                INPUT[i][j] = "."
                diff += 1
            else:
                INPUT[i][j] = "."
        if diff > 0:
            for x in range(si+1, si+1+diff):
                INPUT[x][j] = "O"

    for i in range(len(INPUT)):
        si = -1
        diff = 0
        for j in range(len(INPUT[0])):
            if INPUT[i][j] == "#":
                for x in range(si+1, si+1+diff):
                    INPUT[i][x] = "O"
                si = j
                diff = 0
            elif INPUT[i][j] == "O":
                INPUT[i][j] = "."
                diff += 1
            else:
                INPUT[i][j] = "."
        if diff > 0:
            for x in range(si+1, si+1+diff):
                INPUT[i][x] = "O"

    for j in range(len(INPUT[0])):
        si = len(INPUT)
        diff = 0
        for i in range(len(INPUT)-1, -1, -1):
            if INPUT[i][j] == "#":
                for x in range(si-1, si-1-diff, -1):
                    INPUT[x][j] = "O"
                si = i
                diff = 0
            elif INPUT[i][j] == "O":
                INPUT[i][j] = "."
                diff += 1
            else:
                INPUT[i][j] = "."
        if diff > 0:
            for x in range(si-1, si-1-diff, -1):
                INPUT[x][j] = "O"

    for i in range(len(INPUT)):
        si = len(INPUT[0])
        diff = 0
        for j in range(len(INPUT[0])-1, -1, -1):
            if INPUT[i][j] == "#":
                for x in range(si-1, si-1-diff, -1):
                    INPUT[i][x] = "O"
                si = j
                diff = 0
            elif INPUT[i][j] == "O":
                INPUT[i][j] = "."
                diff += 1
            else:
                INPUT[i][j] = "."
        if diff > 0:
            for x in range(si-1, si-1-diff, -1):
                INPUT[i][x] = "O"

    # for row in INPUT:
    #     print(row)

    loads = 0
    for i in range(len(INPUT)):
        for j in range(len(INPUT[0])):
            if INPUT[i][j] == "O":
                loads += (len(INPUT) - i)

    candidates.append(loads)


# 1 2 3 4 5 6 7 5 6 7(10th)
#         ^(i)  ^(j)
#         4     7
# data[4 + (10 - 4 - 1) % (7 - 4)] = data[4 + 5 % 3] = data[6]
for i in range(len(candidates)-1):
    for j in range(i + 1, len(candidates)):
        match = True
        repeat_count = j - i
        for z in range(i, len(candidates) - repeat_count):
            if candidates[z] != candidates[z + repeat_count]:
                match = False
                break
        if match:
            print(candidates[i + (1000000000 - i - 1) % (j - i)])
            exit()
