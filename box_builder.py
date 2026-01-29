def turn_right():
    turn_left()
    turn_left()
    turn_left()

def build_square():
    repeat 4:
        build_wall()
        move()
        turn_left()

build_square()
