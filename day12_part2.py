INPUT = open("day12_input.txt").read().splitlines()
# ?.?.???????##???????.?.???????##???????.?.???????##???????.?.???????##???????.?.???????##????? [1, 2, 8, 1, 2, 8, 1, 2, 8, 1, 2, 8, 1, 2, 8]
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# INPUT = open("test.txt").read().splitlines() # 525152

def move(springs, arrangements, cal, cache):
    # sprints ["?", "?", "?", "#", "?", "?", "?", "?", "?", "?"]
    # arrangements [4, 4]
    # cal (sprint index, arrangements index, current group count)
    if cal in cache:
        return cache[cal]


    if len(springs) <= cal[0]:
        if cal[2] == 0:
            if len(arrangements) == cal[1]:
                return 1
        else:
            if len(arrangements)-1 == cal[1] and arrangements[-1] == cal[2]:
                return 1
        return 0

    results = 0

    if springs[cal[0]] == ".":
        if cal[2] == 0:
            results += move(springs, arrangements, (cal[0]+1, cal[1], 0), cache)
        elif len(arrangements) <= cal[1] or arrangements[cal[1]] != cal[2]:
            pass
        else:
            results += move(springs, arrangements, (cal[0]+1, cal[1]+1, 0), cache)
    elif springs[cal[0]] == "#":
        results += move(springs, arrangements, (cal[0]+1, cal[1], cal[2]+1), cache)
    else: # ?
        results += move(springs, arrangements, (cal[0]+1, cal[1], cal[2]+1), cache)

        if cal[2] == 0:
            results += move(springs, arrangements, (cal[0]+1, cal[1], 0), cache)
        elif len(arrangements) <= cal[1] or arrangements[cal[1]] != cal[2]:
            pass
        else:
            results += move(springs, arrangements, (cal[0]+1, cal[1]+1, 0), cache)

    cache[cal] = results

    return results

results = 0
for line in INPUT:
    springs, arrangements_txt = line.split()
    arrangements = [int(x) for x in arrangements_txt.split(",")]

    full_sprints = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
    full_arrangements = arrangements + arrangements + arrangements + arrangements + arrangements

    cache = {}
    # print(full_sprints, full_arrangements)
    results += move(full_sprints, full_arrangements, (0, 0, 0), cache)

print(results)
