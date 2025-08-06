'''
Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.
'''

def nestParen(str):
    if len(str) == 0:
        return True
    if str[0] not in '()':
        return nestParen(str[1:])
    if str[-1] not in '()':
        return nestParen(str[:-1])
    # if str[0] not in ['(', ')']: 
    #     return nestParen(str[1:]) 
    # if len(str) == 1:
    #     return False
    # end = 0
    # start = 0
    # if str[0] == '(':
    #     end = -1
    # if str[-1] == ')':
    #     start = 1
    # return nestParen(str[start:end])
    if str[0] == '(' and str[-1] == ')':
        return nestParen(str[1:-1])
    return False

def nestParenGodV(str, depth = 0):
    if len(str) == 0:
        return depth == 0
    if str[0] == '(':
        return nestParenGodV(str[1:], depth + 1)
    if str[0] == ')':
        return nestParenGodV(str[1:], depth - 1)
    return nestParenGodV(str[1:], depth)
  
    
# print(nestParen("((())x)x"))
# print(nestParen("(x)"))
# print(nestParen("(()))"))
# print(nestParen("(())"))
# print(nestParen("((()()))"))

print(nestParenGodV("((())x)x"))
print(nestParenGodV("(x)"))
print(nestParenGodV("(()))"))
print(nestParenGodV("(())"))
print(nestParenGodV("((()()))"))
