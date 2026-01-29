def turn_right():
    turn_left()
    turn_left()
    turn_left()

def square():
    repeat 4:
        build_wall()
        move()
        turn_left()

repeat 3:
    square()
    move()
    move()
