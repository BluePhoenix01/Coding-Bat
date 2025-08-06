def countPair(str):
    if len(str) == 2:
        return 0
    return int(str[0] == str[2]) + countPair(str[1:])

print(countPair("abcb"))
print(countPair("axx"))
print(countPair("axax"))
print(countPair("axaxa"))