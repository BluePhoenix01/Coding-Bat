def strDist(str, sub):
    if len(str) < len(sub):
        return 0
    start = 1
    if str == sub:
        return len(str)
    if str[-len(sub):] == sub:
        return len(str)
    if str[0:len(sub)] == sub:
        start = 0
    return strDist(str[start:-1], sub)
    
print(strDist('catcowcat', 'cat'))
print(strDist('catcowcat', 'cow'))  
print(strDist('catcowcat', 'dog'))