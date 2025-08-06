'''
Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
'''

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