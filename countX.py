def countX(str):
    if len(str) == 0:
        return 0
    elif str[0] == 'x':
        return 1 + countX(str[1:])
    else:
        return countX(str[1:])