def powerN(base, n):
    if n == 0:
        return 1
    else:
        return base * powerN(base, n - 1)
    
print(powerN(2, 3))
print(powerN(3, 3))
print(powerN(4, 3))