import random
def doAgain():
    again = raw_input("Want to draw something else? y/n \n")
    if again == "y":
        chooseShape()
    elif again == "n":
        print "Awesome, have a nice day!"
    else:
        randomMessage()
        doAgain()
def randomMessage():
    num = random.randint(1, 7)
    if num == 1:
        print "Your mother was a hampster!"
    elif num == 2:
        print "Pool on the roof has a leak."
    elif num == 3:
        print "Don't do that again."
    else:
        print "Invalid input"
def chooseShape():
    star = "*"
    shape = int(raw_input("Enter a number to choose what to paint: \n 1 for Triangles \n 2 for Rectangles \n 3 for Boxes \n"))
    def drawRectangle(length, width):
        for row in range(length):
            print star * width
    def drawTriangle(height):
        height2 = range(1, height * 2, 2)
        width = height * 2 - 1
        star = "*"
        space = " "
        for row in height2:
            width2 = width - row
            spaces = width2 / 2
            print  space * spaces + star * row + space * spaces
    def drawBox(width, height):
        height2 = height + 1
        width2 = width - 2
        star = "*"
        space = " "
        lines = range(1, height2)
        for line in lines :
            if line == 1:
                print star * width
            elif line == height :
                print star * width
            else :
                print star + space * width2 + star
    if shape == 1:
        height = int(raw_input('Enter Triangle height: '))
        drawTriangle(height)
        doAgain()
    elif shape == 2:
        length = int(raw_input('Enter Rectangle length: '))
        width = int(raw_input('Enter Rectangle width: '))
        drawRectangle(length, width)
        doAgain()
    elif shape == 3:
        width = int(raw_input('Box width? '))
        height = int(raw_input('Box height? '))
        drawBox(width, height)
        doAgain()
    else:
        print "Error, invalid number."
        doAgain()
shape = chooseShape()