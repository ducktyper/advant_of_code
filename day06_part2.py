TXT = open("day06_input.txt").read().splitlines()

TIME = int("".join(TXT[0].split(":")[1].split()))
DISTANCE = int("".join(TXT[1].split(":")[1].split()))

results = 0
for j in range(1, TIME + 1):
    if DISTANCE < (TIME - j) * j:
        results += 1

print(results)

