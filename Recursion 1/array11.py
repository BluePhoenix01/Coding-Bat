'''
Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
'''

def array11(nums, idx = 0):
    if idx == len(nums):
        return False
    return int(nums[idx] == 11) + array11(nums, idx + 1)

print(array11([1, 2, 11]))
print(array11([1, 11, 11]))
print(array11([11, 11, 11])) 