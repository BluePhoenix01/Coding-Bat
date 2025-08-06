'''
Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
'''

def array220(nums, idx = 0):
    if idx == len(nums)-1:
        return False
    return True if nums[idx]*10 == nums[idx+1] else array220(nums, idx + 1)

print(array220([1, 2, 20]))
print(array220([1, 2, 30]))
print(array220([2, 20, 2]))