def countHi2(str):
    if len(str) == 1:
        return 0
    return countHi2(str[2:]) if str[0] == 'x' else int(str[0:2] == 'hi') + countHi2(str[1:])

print(countHi2('hihi'))
print(countHi2('xhixhi'))
print(countHi2('hi'))