results = 0

for line in open("day02_input.txt").read().splitlines():
    valid = True
    game_txt, cube_sets_txt = line.split(":")
    for cube_set_txt in cube_sets_txt.split(";"):
        for cube in cube_set_txt.split(","):
            num_txt, colour = cube.strip().split(" ")
            if colour == "red" and int(num_txt) > 12:
                valid = False
            elif colour == "green" and int(num_txt) > 13:
                valid = False
            elif colour == "blue" and int(num_txt) > 14:
                valid = False

    if valid:
        results += int(game_txt.split(" ")[1])

print(results)
