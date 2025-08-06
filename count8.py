def count8(n):
    if n == 0:
        return 0
    else:
        return int(n%10 == 8) + (2 * count8(n//10) if n%10 == 8 and(n//10)%10 == 8 else count8(n//10))
    
    
print(count8(8818))
print(count8(8))
print(count8(123))