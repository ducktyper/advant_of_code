TXT = open("day08_input.txt").read().splitlines()

STEPS = TXT[0]

MAP = {}
for line in TXT[2:]:
    MAP[line[0:3]] = [line[7:10], line[12:15]]

current = "AAA"
results = 0
finished = False
while not finished:
    for step in STEPS:
        current = MAP[current][0 if step == "L" else 1]
        results += 1
        if current == "ZZZ":
            finished = True
            break

print(results)
