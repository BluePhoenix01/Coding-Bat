def changePi(str):
    if len(str) == 0:
        return ""
    if str[0:2] == 'pi':
        return '3.14' + changePi(str[2:])
    else:
        return str[0] + changePi(str[1:])

print(changePi('pipi'))
print(changePi('pip'))
print(changePi('hi'))