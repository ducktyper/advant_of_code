TXT = open("day08_input.txt").read().splitlines()

STEPS = TXT[0]

MAP = {}
current = []
for line in TXT[2:]:
    MAP[line[0:3]] = [line[7:10], line[12:15]]
    if line[2] == "A":
        current.append(line[0:3])

def isFinished(current):
    for x in current:
        if x[2] != "Z":
            return False
    return True

counter = 0

loop = [0 for x in current]
while 0 in loop:
    for step in STEPS:
        counter += 1
        for i in range(len(current)):
            current[i] = MAP[current[i]][0 if step == "L" else 1]

            if current[i][2] == "Z" and loop[i] == 0:
                loop[i] = counter

results = 0

move = max(loop)
while True:
    results += move
    found = True
    for i in range(len(loop)):
         if results % loop[i] != 0:
             found = False
             break
    if found:
        break

print(results)
