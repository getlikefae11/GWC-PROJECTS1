from turtle import *
import math

# Name your Turtle.
Favour = Turtle()
Favour.penup()
# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
Favour.setposition(x_pos, y_pos)

### Write your code below:
Favour.pendown()
for x in range (3):
    Favour.right(120)
    Favour.forward(100)
Favour.penup()
# Close window on click.
exitonclick()
