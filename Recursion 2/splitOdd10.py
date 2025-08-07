# Given an array of ints, is it possible to divide the ints into two groups, so that the sum of one group is a multiple of 10, and the sum of the other group is odd. 
# Every int must be in one group or the other. Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive 
# helper from splitOdd10(). (No loops needed.)

def splitOdd10(nums):
    if sum(nums) % 2 == 0:
        return False
    def recursiveHelper(start, nums, target):
        if start >= len(nums):
            return target % 10 == 0
        if target % 10 == 0:
            return True
        if recursiveHelper(start + 1, nums, target + nums[start]):
            return True
        if recursiveHelper(start + 1, nums, target):
            return True
        return False
    
    return recursiveHelper(0, nums, 0)

print(splitOdd10([5, 5, 4]))
print(splitOdd10([5, 5, 10]))
print(splitOdd10([5, 10, 15]))
print(splitOdd10([7, 3, 3]))