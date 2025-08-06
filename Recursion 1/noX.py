'''
Given a string, compute recursively a new string where all the 'x' chars have been removed.
'''

def noX(str):
    if len(str) == 0:
        return ""
    if str[0] == 'x':
        return noX(str[1:])
    else:
        return str[0] + noX(str[1:])
    
print(noX('xaxb'))
print(noX('abc'))
print(noX('xx'))