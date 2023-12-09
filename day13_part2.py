INPUT = open("day13_input.txt").read().splitlines()

def smuge_equal(a, b):
    if a == b:
        return False
    aa = bin(abs(a))[2:]
    bb = bin(abs(b))[2:]
    if len(aa) > len(bb):
        bb = "0" * (len(aa) - len(bb)) + bb
    else:
        aa = "0" * (len(bb) - len(aa)) + aa
    diff_count = 0
    for i in range(len(aa)):
        if aa[i] != bb[i]:
            diff_count += 1
    return diff_count == 1

def solve(puzzle):
    holizontal = []
    results = 0
    for i in range(len(puzzle)):
        v = []
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == "#":
                v.append("1")
            else:
                v.append("0")
        holizontal.append(int("".join(v), 2))

    for i in range(len(holizontal)-1):
        if holizontal[i] == holizontal[i+1] or smuge_equal(holizontal[i], holizontal[i+1]):
            smuge = 1 if smuge_equal(holizontal[i], holizontal[i+1]) else 0
            s, f, match = i, i+1, True
            s -= 1
            f += 1
            while (s >= 0 and f < len(holizontal)):
                if holizontal[s] != holizontal[f] and not smuge_equal(holizontal[s], holizontal[f]):
                    match = False
                    break
                if smuge_equal(holizontal[s], holizontal[f]):
                    smuge += 1
                s -= 1
                f += 1
            if match and smuge == 1:
                results += (i + 1) * 100
                break

    vertical = []
    for j in range(len(puzzle[0])):
        v = []
        for i in range(len(puzzle)):
            if puzzle[i][j] == "#":
                v.append("1")
            else:
                v.append("0")
        vertical.append(int("".join(v), 2))

    for i in range(len(vertical)-1):
        if vertical[i] == vertical[i+1] or smuge_equal(vertical[i], vertical[i+1]):
            smuge = 1 if smuge_equal(vertical[i], vertical[i+1]) else 0
            s, f, match = i, i+1, True
            s -= 1
            f += 1
            while (s >= 0 and f < len(vertical)):
                if vertical[s] != vertical[f] and not smuge_equal(vertical[s], vertical[f]):
                    match = False
                    break
                if smuge_equal(vertical[s], vertical[f]):
                    smuge += 1
                s -= 1
                f += 1
            if match and smuge == 1:
                results += (i + 1)
                break

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
