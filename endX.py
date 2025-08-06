def endX(str):
    if len(str) == 0:
        return ""
    if str[0] == 'x':
        return endX(str[1:]) + 'x'
    else:
        return str[0] + endX(str[1:])

print(endX("xxre"))
print(endX("xxhixx"))
print(endX("xhixhix"))