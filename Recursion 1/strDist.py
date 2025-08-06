'''
Given a string and a non-empty substring sub, compute recursively the largest substring which starts and ends with sub and return its length.
'''

def strDist(str, sub):
    if len(str) < len(sub):
        return 0
    start = 1
    end = -1
    if str[-len(sub):] == sub:
        end = len(str)
    if str[:len(sub)] == sub:
        start = 0
    if str[-len(sub):] == sub and str[:len(sub)] == sub:
        return len(str)
    return strDist(str[start:end], sub)
    
print(strDist('catcowcat', 'cat'))
print(strDist('catcowcat', 'cow'))  
print(strDist('catcowcat', 'dog'))
print(strDist('cowcatcat', 'cat'))