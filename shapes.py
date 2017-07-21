from turtle import *
import math

# Name your Turtle.
Favour = Turtle()
Favour.penup
# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
Favour.setposition(x_pos, y_pos)

### Write your code below:
#pencolor(pink)
Favour.begin_fill()
Favour.fillcolor("pink")
Favour.pendown()
for x in range (4):
    Favour.right(90)
    Favour.forward(50)
Favour.penup()
Favour.end_fill()
# Close window on click.
exitonclick()
