INPUT = open("day15_input.txt").read().strip().split(",")

boxes = [[] for _ in range(256)]

for string in INPUT:
    result = 0
    for c in string:
        if c in ("-", "="):
            break
        result = ((result + ord(c)) * 17) % 256
    box = boxes[result]
    if string[-1] == "-":
        new_box = []
        for item in box:
            if item[0] != string[:-1]:
                new_box.append(item)
        boxes[result] = new_box
    else:
        label, number_str = string.split("=")
        found = False
        for x in box:
            if x[0] == label:
                x[1] = int(number_str)
                found = True
                break
        if not found:
            box.append([label, int(number_str)])

results = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        results += (i + 1) * (j + 1) * boxes[i][j][1]

print(results)
