from turtle import *

# forward(100)
# right(45)
# forward(150)

shape('turtle')
def square():
    for i in range(4):
        forward(100)
        right(90)

for i in range(60):
    square()
    right(5)

#
# # from turtle import Turtle, Screen
# jabba = Turtle()
# print(jabba)

my_screen = Screen()
# print(my_screen.canvheight)
my_screen.exitonclick()