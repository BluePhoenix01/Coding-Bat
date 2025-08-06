'''
Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
'''

def count8(n):
    if n == 0:
        return 0
    else:
        return int(n%10 == 8) + (2 * count8(n//10) if n%10 == 8 and(n//10)%10 == 8 else count8(n//10))
    
    
print(count8(8818))
print(count8(8))
print(count8(123))