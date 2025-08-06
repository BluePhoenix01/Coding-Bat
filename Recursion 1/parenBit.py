'''
Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)".
'''

def parenBit(str):
    if len(str) == 0:
        return ""
    start = 1
    end = -1
    if str[-1] == ")":
        end = len(str)
    if str[0] == "(":
        start = 0
    if str[-1] == ")" and str[0] == "(":
        return str
    return parenBit(str[start:end])
    
print(parenBit("abc(xyz)ahyjgsb"))
print(parenBit("abcxyzahy()jgsb"))
print(parenBit("(abcxyz)ahyjgsb"))
print(parenBit("abcxyzah(yjgsb)"))
