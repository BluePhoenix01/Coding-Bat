def count11(str):
    if len(str) == 1:
        return 0
    if str == '11':
        return 1
    if str[0:2] == '11':
        return 1 + count11(str[2:])
    else :
        return count11(str[1:])

print(count11('11abc11'))
print(count11('abc11x11x11'))
print(count11('111'))