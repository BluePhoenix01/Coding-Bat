'''
Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
'''

def allStar(str):
    if len(str) <= 1:
        return str
    return str[0] + "*" + allStar(str[1:])

print(allStar("hello"))
print(allStar("abc"))
print(allStar(""))