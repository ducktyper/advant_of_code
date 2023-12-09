DATA = open("day17_input.txt").read().splitlines()
DATA = open("test.txt").read().splitlines()

i_max, j_max = len(DATA)-1, len(DATA[0])-1
start = (0, 0)
destination = (i_max, j_max)
# cache_future = {} # (location, direction, n_straight): current/future loss
cache_past = {} # (location, direction, n_straight): loss before the location

min_results = float("inf")

def get_next_location(location, direction):
    i, j = location
    if direction == "U":
        ic, jc = i-1, j
    elif direction == "D":
        ic, jc = i+1, j
    elif direction == "L":
        ic, jc = i, j-1
    elif direction == "R":
        ic, jc = i, j+1
    return (ic, jc)

def out_of_range(location):
    i, j = location
    return i < 0 or j < 0 or i > i_max or j > j_max

def get_val(location):
    i, j = location
    return int(DATA[i][j])

def can_move(location, direction, n_straight, next_direction):
    # Move in grid
    next_location = get_next_location(location, next_direction)
    if out_of_range(next_location):
        return False

    # No straight for longer than 3 moves
    if direction == next_direction and n_straight == 3:
        return False

    # No reverse
    if direction == "R" and next_direction == "L":
        return False
    if direction == "L" and next_direction == "R":
        return False
    if direction == "U" and next_direction == "D":
        return False
    if direction == "D" and next_direction == "U":
        return False

    return True

def move(location, direction, n_straight, loss_so_far):
    # location: (i, j)
    # direction: U, D, L, R
    # n_straight: 1, 2, 3
    global min_results

    next_location = get_next_location(location, direction)

    if loss_so_far > min_results:
        return

    # Less/equal loss is possible to this location
    for x in range(1, n_straight+1):
        if (location, direction, x) in cache_past:
            if cache_past[(location, direction, x)] < loss_so_far:
                return
    cache_past[(location, direction, n_straight)] = loss_so_far

    current_loss = get_val(next_location)

    if next_location == destination:
        # print(loss_so_far + current_loss)
        if min_results > loss_so_far + current_loss:
            min_results = loss_so_far + current_loss
        return

    if can_move(next_location, direction, n_straight, "R"):
        move(next_location, "R", n_straight + 1 if direction == "R" else 1, loss_so_far + current_loss)
    if can_move(next_location, direction, n_straight, "D"):
        move(next_location, "D", n_straight + 1 if direction == "D" else 1, loss_so_far + current_loss)
    if can_move(next_location, direction, n_straight, "L"):
        move(next_location, "L", n_straight + 1 if direction == "L" else 1, loss_so_far + current_loss)
    if can_move(next_location, direction, n_straight, "U"):
        move(next_location, "U", n_straight + 1 if direction == "U" else 1, loss_so_far + current_loss)

move(start, "R", 1, 0)
move(start, "D", 1, 0)

print(min_results)
