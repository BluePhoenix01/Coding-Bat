'''
Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
'''

def array6(nums, idx = 0):
    if idx == len(nums):
        return False
    if nums[idx] == 6:
        return True
    return array6(nums, idx + 1)

print(array6([1, 2, 6]))
print(array6([1, 2, 3]))
print(array6([6, 2, 3]))