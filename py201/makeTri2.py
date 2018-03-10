def makeTri(height):
    height2 = range(1, height * 2, 2)
    width = height * 2 - 1
    star = "*"
    space = " "
    for row in height2:
        width2 = width - row
        spaces = width2 / 2
        print  space * spaces + star * row + space * spaces
height = int(raw_input('Enter Triangle height: '))
makeTri(height)