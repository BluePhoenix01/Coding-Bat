# Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with these additional 
# constraints: all multiples of 5 in the array must be included in the group. If the value immediately following a multiple of 5 is 1, it must not be chosen.
# (No loops needed.)

def groupSum5(start, nums, target):
    if start >= len(nums):
        return target == 0
    if nums[start]%5 == 0:
        if start+1 < len(nums) and nums[start+1] != 1:
            return groupSum5(start+1, nums, target - nums[start])
        return groupSum5(start+2, nums, target - nums[start])
    if groupSum5(start+1, nums, target - nums[start]):
        return True
    if groupSum5(start+1, nums, target):
        return True
    return False     
print(groupSum5(0, [2, 5, 10], 15))
print(groupSum5(0, [2, 5, 10], 12))
print(groupSum5(0, [2, 5, 1, 10, 1], 18))
    