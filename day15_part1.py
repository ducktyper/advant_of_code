INPUT = open("day15_input.txt").read().strip().split(",")

results = 0
for string in INPUT:
    result = 0
    for c in string:
        result = ((result + ord(c)) * 17) % 256
    results += result

print(results)
