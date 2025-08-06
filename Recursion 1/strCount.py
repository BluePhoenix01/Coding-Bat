'''
Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.
'''

def strCount(str, subStr):
    if len(str) < len(subStr):
        return 0
    if str[:len(subStr)] == subStr:
        return 1 + strCount(str[len(subStr):], subStr)
    else:
        return strCount(str[1:], subStr)

print(strCount('catcowcat', 'cat'))
print(strCount('catcowcat', 'cow'))
print(strCount('catcowcat', 'dog'))