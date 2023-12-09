results = 0

for line in open("day02_input.txt").read().splitlines():
    valid = True
    game_txt, cube_sets_txt = line.split(":")
    max_red = 0
    max_green = 0
    max_blue = 0
    for cube_set_txt in cube_sets_txt.split(";"):
        for cube in cube_set_txt.split(","):
            num_txt, colour = cube.strip().split(" ")
            if colour == "red" and int(num_txt) > max_red:
                max_red = int(num_txt)
            elif colour == "green" and int(num_txt) > max_green:
                max_green = int(num_txt)
            elif colour == "blue" and int(num_txt) > max_blue:
                max_blue = int(num_txt)

    results += max_red * max_green * max_blue

print(results)
