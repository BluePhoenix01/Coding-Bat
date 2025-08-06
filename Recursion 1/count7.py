'''
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
'''

def count7(n):
    if n == 0:
        return 0
    else:
        return int(n%10 == 7) + count7(n//10)

print(count7(717))
print(count7(7))
print(count7(123))