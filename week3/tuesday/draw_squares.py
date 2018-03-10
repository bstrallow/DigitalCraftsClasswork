from turtle import *
from drawShapes import *
coord_list = [
    (-100, 100, 100),
    (100, 100, 60),
    (100, -100, 300),
    (-100, -100, 15)
]
for coord in coord_list:
    up()
    home()
    x, y, size = coord
    #When you define two variables at the same time like this, it will take the first and second items in that list/tuple/string, respectively.
    setheading(270)
    forward(x)
    setheading(0)
    forward(y)
    down()
    drawSquare(size)

mainloop()