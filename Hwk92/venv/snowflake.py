# Python program to print partial Koch Curve.
# importing the libraries : turtle standard
# graphics library for python
from turtle import *

# function to create koch snowflake or koch curve
def snowflake(sizeSide, levels):
    if levels == 0:
        forward(sizeSide)
        return
    sizeSide /= 3.0
    snowflake(sizeSide, levels - 1)
    left(60)
    snowflake(sizeSide, levels - 1)
    right(120)
    snowflake(sizeSide, levels - 1)
    left(60)
    snowflake(sizeSide, levels - 1)

# main function
if __name__ == "__main__":
    # set up screen forensics
    size = 200
    screen = Screen()
    screen.setup(size + 100, size + 100)
    # # if setup not larger than screensize, scrollbars will appear
    # screen.screensize(size, size)

    screen.title("Blue Turtle on Green Background")
    # defining the speed of the turtle

    # set pen forensics
    bgcolor("#93EC94")
    pencolor("#578DBE")
    pensize(3)

    #hide cursor
    hideturtle()
    ht()

    speed(0)

    # Pull the pen up – no drawing when moving.
    penup()
    sety(size/3.0)

    # Move the turtle backward by distance,
    # opposite to the direction the turtle
    # is headed.
    # Do not change the turtle’s heading.
    backward(size / 2.0)

    # Pull the pen down – drawing when moving.
    pendown()

    for i in range(3):
        snowflake(size, 2)
        right(120)

    # To control the closing windows of the turtle
    screen.exitonclick()

