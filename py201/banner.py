whatSay = raw_input('What will your banner say? ')
height = range(1, 4)
width = len(whatSay) + 2
star = "*"
for row in height:
    if row == 2:
        print star + whatSay + star
    else:
        print star * width    