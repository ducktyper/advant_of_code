GRID = open("day05_input.txt").read().splitlines()

seeds = [int(x) for x in GRID[0][7:].split(" ")]


mappings = []
for line in GRID[2:]:
    if line == "":
        for i in range(len(seeds)):
            val = seeds[i]
            for destination, source, length in mappings:
                if val >= source and val < source + length:
                    seeds[i] = destination + val - source
                    break
        mappings = []
    elif line[-1] != ":":
        mappings.append([int(x) for x in line.split(" ")])

if len(mappings) > 0:
    for i in range(len(seeds)):
        val = seeds[i]
        for destination, source, length in mappings:
            if val >= source and val < source + length:
                seeds[i] = destination + val - source
                break
    mappings = []

print(min(seeds))

