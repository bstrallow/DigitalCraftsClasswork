height = range(1, 8, 2)
width = 7
star = "*"
space = " "
for row in height:
    width2 = width - row
    spaces = width2 / 2
    print  space * spaces + star * row + space * spaces