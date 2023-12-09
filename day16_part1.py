DATA = open("day16_input.txt").read().splitlines()

visited = {} # (i, j): [directions]

def move(position, direction):
    i, j = position
    if i < 0 or j < 0 or i >= len(DATA) or j >= len(DATA[0]):
        return

    if position not in visited:
        visited[position] = []
    if direction in visited[position]:
        return
    visited[position].append(direction)

    val = DATA[i][j]
    if direction == "L":
        if val in (".", "-"):
            j_next = j-1
            while j_next >= 0 and DATA[i][j_next] in (".", "-"):
                position_next = (i, j_next)
                if position_next not in visited:
                    visited[position_next] = []
                if direction in visited[position_next]:
                    return
                visited[position_next].append(direction)
                j_next -= 1
            move((i, j_next), direction)
        elif val == "|":
            move((i-1, j), "U")
            move((i+1, j), "D")
        elif val == "/":
            move((i+1, j), "D")
        elif val == "\\":
            move((i-1, j), "U")
    elif direction == "R":
        if val in (".", "-"):
            j_next = j+1
            while j_next < len(DATA[0]) and DATA[i][j_next] in (".", "-"):
                position_next = (i, j_next)
                if position_next not in visited:
                    visited[position_next] = []
                if direction in visited[position_next]:
                    return
                visited[position_next].append(direction)
                j_next += 1
            move((i, j_next), direction)
        elif val == "|":
            move((i-1, j), "U")
            move((i+1, j), "D")
        elif val == "/":
            move((i-1, j), "U")
        elif val == "\\":
            move((i+1, j), "D")
    elif direction == "U":
        if val in (".", "|"):
            i_next = i-1
            while i_next >= 0 and DATA[i_next][j] in (".", "|"):
                position_next = (i_next, j)
                if position_next not in visited:
                    visited[position_next] = []
                if direction in visited[position_next]:
                    return
                visited[position_next].append(direction)
                i_next -= 1
            move((i_next, j), direction)
        elif val == "-":
            move((i, j-1), "L")
            move((i, j+1), "R")
        elif val == "/":
            move((i, j+1), "R")
        elif val == "\\":
            move((i, j-1), "L")
    elif direction == "D":
        if val in (".", "|"):
            i_next = i+1
            while i_next < len(DATA) and DATA[i_next][j] in (".", "|"):
                position_next = (i_next, j)
                if position_next not in visited:
                    visited[position_next] = []
                if direction in visited[position_next]:
                    return
                visited[position_next].append(direction)
                i_next += 1
            move((i_next, j), direction)
        elif val == "-":
            move((i, j-1), "L")
            move((i, j+1), "R")
        elif val == "/":
            move((i, j-1), "L")
        elif val == "\\":
            move((i, j+1), "R")

move((0, 0), "R")

print(len(visited))
