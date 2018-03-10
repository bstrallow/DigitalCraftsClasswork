from turtle import *
def drawTriangle(size = 100):
    for i in range(3):
        forward(size)
        left(120)
    #works
def drawCircle(size = 100):
    def drawCircle(size = 100):
    circle(size)
    #works, using already existing function.
def drawPentagon(size = 100):
    for i in range(5):
        forward(size)
        left(72)
    #works
def drawHexagon(size = 100):
    for i in range(6):
        forward(size)
        left(60)
    #works
def drawOctagon(size = 100):
    for i in range(8):
        forward(size)
        left(45)
def drawStar(size = 100):
    for i in range(5):
        right(144)
        forward(size)
    #works
def drawSquare(size = 100):
    for i in range(4):
        forward(size)
        left(90)
    #works

if __name__ == '__main__':
    drawSquare()
    up()
    forward(200)
    down()
    drawTriangle()
    mainloop()