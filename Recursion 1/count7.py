def count7(n):
    if n == 0:
        return 0
    else:
        return int(n%10 == 7) + count7(n//10)

print(count7(717))
print(count7(7))
print(count7(123))