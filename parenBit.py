def parenBit(str):
    if len(str) == 0:
        return ""
    start = 1
    if str[-1] == ")":
        return str 
    if str[0] == "(":
        start = 0
    return parenBit(str[start:-1])
    
print(parenBit("abc(xyz)ahyjgsb"))
print(parenBit("abcxyzahyjgsb"))
print(parenBit("abc(xyz)ahyjgsb"))
