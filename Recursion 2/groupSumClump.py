# Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target, with this additional 
# constraint: if there are numbers in the array that are adjacent and the identical value, they must either all be chosen, or none of them chosen. 
# For example, with the array {1, 2, 2, 2, 5, 2}, either all three 2's in the middle must be chosen or not, all as a group. (one loop can be used to find 
# the extent of the identical values).

def groupSumClump(start, nums, target):
    print(f"Checking start={start}, nums={nums[start:]}, target={target}")
    if start >= len(nums):
        return target == 0
    i = 1
    while start+i < len(nums) and nums[start] == nums[start+i]:
        i += 1
    if groupSumClump(start+i, nums, target - nums[start]*i):
        return True
    if groupSumClump(start+i, nums, target):
        return True
    return False

# print(groupSumClump(0, [1, 2, 2, 2, 5, 2], 9))
print(groupSumClump(0, [1, 2, 2, 2, 5, 2], 8))
# print(groupSumClump(0, [1, 2, 2, 2, 5, 2], 10))