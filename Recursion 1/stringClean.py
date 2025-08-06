'''
Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char. So "yyzzza" yields "yza"
'''

def stringClean(str):
    if len(str) == 1:
        return str
    return stringClean(str[1:]) if str[0] == str[1] else str[0] + stringClean(str[1:])

print(stringClean("abbccc"))
print(stringClean("abb"))
print(stringClean("abc"))
print(stringClean("aa"))