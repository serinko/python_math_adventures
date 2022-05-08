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

for i in range(70):
    triangle(300)
    right(5)

#
# # from turtle import Turtle, Screen
# jabba = Turtle()
# print(jabba)

my_screen = Screen()
# print(my_screen.canvheight)
my_screen.exitonclick()