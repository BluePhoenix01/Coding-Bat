'''
Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
'''

def countHi(str):
    if len(str) == 0:
        return 0
    elif str[0:2] == 'hi':
        return 1 + countHi(str[2:])
    else:
        return countHi(str[1:])

print(countHi('hihi'))
print(countHi('xhixhi'))
print(countHi('hi'))