results = 0

num_strs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for line in open("day01_input.txt").read().splitlines():
    found = False
    for i in range(len(line)):
        for j in range(len(num_strs)):
            if line[i] == num_strs[j]:
                if not found:
                    results += j * 10
                    found = True

    found = False
    for i in reversed(range(len(line))):
        for j in range(len(num_strs)):
            if line[i] == num_strs[j]:
                if not found:
                    results += j
                    found = True

print(results)
