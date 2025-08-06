def changeXY(str):
    if len(str) == 0:
        return ""
    if str[0] == 'x':
        return 'y' + changeXY(str[1:])
    else:
        return str[0] + changeXY(str[1:])
    
print(changeXY('xix'))
print(changeXY('xixhi'))
print(changeXY('hi'))