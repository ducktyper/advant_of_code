TXT = open("day09_input.txt").read().splitlines()

def all_zero(values):
    for x in values:
        if x != 0:
            return False
    return True

results = 0
for line in TXT:
    history = [[int(x) for x in line.split()]]
    while not all_zero(history[-1]):
        next_history = []
        for i in range(len(history[-1])-1):
            next_history.append(history[-1][i+1] - history[-1][i])
        history.append(next_history)

    results += sum([x[-1] for x in history])

print(results)
