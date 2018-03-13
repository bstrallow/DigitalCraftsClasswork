from turtle import *
from drawShapes import *
shapes = (drawTriangle(), draw)
def nextShape(distance = 100):
    up()
    forward(distance)
    down()
def drawShapes(shapes):
