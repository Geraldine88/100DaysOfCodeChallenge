def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_top():
    turn_left()
    move()


def turn_down():
    turn_right()
    move()


def one_rep():
    # climb up
    turn_left()
    while wall_on_right():
        move()

    # move over the hurdle
    turn_right()
    move()

    # climb down
    turn_right()
    while front_is_clear():
        move()

    # face forward
    turn_left()


# n = 6
# for _ in range(n):
#    one_rep()

count_moves = 0
while not at_goal():
    if wall_in_front():
        one_rep()
        count_moves += 1
    else:
        move()
        count_moves += 1
print(f'Reeborg actually had {count_moves} hurdle(s)')

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
