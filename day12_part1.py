INPUT = open("day12_input.txt").read().splitlines()

counter = [0]

def move(springs, arrangements, cal, counter):
    # cal (index, nth group, group count)
    if len(springs) <= cal[0]:
        if cal[2] == 0:
            if len(arrangements) == cal[1]:
                counter[0] += 1
        else:
            if len(arrangements)-1 == cal[1] and arrangements[-1] == cal[2]:
                counter[0] += 1
        return

    if springs[cal[0]] == ".":
        if cal[2] == 0:
            move(springs, arrangements, (cal[0]+1, cal[1], 0), counter)
        elif len(arrangements) <= cal[1] or arrangements[cal[1]] != cal[2]:
            return
        else:
            move(springs, arrangements, (cal[0]+1, cal[1]+1, 0), counter)
    elif springs[cal[0]] == "#":
        move(springs, arrangements, (cal[0]+1, cal[1], cal[2]+1), counter)
    else: # ?
        move(springs, arrangements, (cal[0]+1, cal[1], cal[2]+1), counter)
        if cal[2] == 0:
            move(springs, arrangements, (cal[0]+1, cal[1], 0), counter)
        elif len(arrangements) <= cal[1] or arrangements[cal[1]] != cal[2]:
            return
        else:
            move(springs, arrangements, (cal[0]+1, cal[1]+1, 0), counter)

for line in INPUT:
    springs, arrangements_txt = line.split()
    arrangements = [int(x) for x in arrangements_txt.split(",")]

    move(springs, arrangements, (0, 0, 0), counter)

print(counter[0])
