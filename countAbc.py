def countAbc(str):
    if len(str) == 2:
        return 0
    return int(str[0:3] == 'abc' or str[0:3] == 'aba') + countAbc(str[1:])

print(countAbc('abc'))
print(countAbc('ababc'))
print(countAbc('abaxc'))
        