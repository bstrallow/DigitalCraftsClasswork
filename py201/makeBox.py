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
width = int(raw_input('Box width? '))
height = int(raw_input('Box height? '))
drawBox(width, height)