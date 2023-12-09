TXT = open("day06_input.txt").read().splitlines()

TIMES = TXT[0].split(":")[1].split()
DISTANCES = TXT[1].split(":")[1].split()

results = 1

for i in range(len(TIMES)):
    time, distance = int(TIMES[i]), int(DISTANCES[i])
    matches = 0
    for j in range(1, time + 1):
        if distance < (time - j) * j:
            matches += 1
    results *= matches

print(results)

