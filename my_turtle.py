from turtle import *

# forward(100)
# right(45)
# forward(150)

shape('turtle')
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)



#
# # from turtle import Turtle, Screen
# jabba = Turtle()
# print(jabba)

def polygon(sides=6, sidelength=100):
    for i in range(sides):
        forward(sidelength)
        turn_angle = 360/sides
        right(int(turn_angle))

# length = 5
# for i in range(60):
#     square(length)
#     length += 5
#     right(5)

def star():
    for i in range(5):
        forward(300)
        right(144)

star()

my_screen = Screen()
# print(my_screen.canvheight)
my_screen.exitonclick()

