# Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such that the group sums to the given target? 
# However, with the additional constraint that all 6's must be chosen. (No loops needed.)

def groupSum6(start, nums, target):
    print(f"Checking start={start}, nums={nums[start:]}, target={target}")
    if start >= len(nums):
        return target == 0
    if nums[start] == 6:
        return groupSum6(start + 1, nums, target - nums[start])
    if groupSum6(start + 1, nums, target - nums[start]):
        return True
    if groupSum6(start + 1, nums, target):
        return True
    return False
            
    
# print(groupSum6(0, [2, 4, 6], 12))
print(groupSum6(0, [2, 4, 6], 10))
# print(groupSum6(0, [2, 4, 6], 14))
