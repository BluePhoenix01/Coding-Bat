#Given an array of ints, is it possible to divide the ints into two groups, so that the sums of the two groups are the same. Every int must be in one 
# group or the other. Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive helper from splitArray().
# (No loops needed.)

def splitArray(nums):
    if sum(nums) % 2 != 0:
        return False
    def recursiveHelper(start, nums, target):
        if start >= len(nums):
            return target == 0
        if recursiveHelper(start + 1, nums, target-nums[start]):
            return True
        if recursiveHelper(start+1, nums, target):
            return True
        return False
    
    return recursiveHelper(0, nums, sum(nums)/2)

print(splitArray([2, 2]))
print(splitArray([2, 3]))
print(splitArray([2, 4, 2]))
print(splitArray([2, 3, 4]))
        
        