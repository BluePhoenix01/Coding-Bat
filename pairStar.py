def pairStar(str):
    if len(str) == 1:
        return str
    if str[0] == str[1]:
        return str[0] + "*" + pairStar(str[1:])
    else:
        return str[0] + pairStar(str[1:])
    
print(pairStar('hello'))
print(pairStar('xxyy'))
print(pairStar('aaaa'))