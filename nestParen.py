def nestParen(str):
    if len(str) == 0:
        return True
    if str[0].isalnum(): 
        return nestParen(str[1:]) 
    if len(str) == 1:
        return False
    end = 0
    start = 0
    if str[0] == '(':
        end = -1
    if str[-1] == ')':
        start = 1
    return nestParen(str[start:end])

print(nestParen("((()))"))
print(nestParen("(x)"))
print(nestParen("(()))"))