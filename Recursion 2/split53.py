# Given an array of ints, is it possible to divide the ints into two groups, so that the sum of the two groups is the same, with these constraints: all the values
# that are multiple of 5 must be in one group, and all the values that are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops needed.)

def split53(nums):
    if sum(nums) % 2 != 0:
        return False
    def recursiveHelper(start, nums, target):
        if start >= len(nums):
            return target == 0
        if nums[start] % 5 == 0:
            return recursiveHelper(start + 1, nums, target - nums[start])
        if nums[start] % 3 == 0:
            return recursiveHelper(start + 1, nums, target)
        if recursiveHelper(start + 1, nums, target - nums[start]):
            return True
        if recursiveHelper(start + 1, nums, target):
            return True
        return False
    
    return recursiveHelper(0, nums, sum(nums)//2)

# print(split53([5, 3, 1, 2, 4]))
# print(split53([5, 3, 1, 2, 4, 6]))
# print(split53([5, 3, 1, 2, 4, 6, 9]))
# print(split53([5, 1, 3, 3]))

print(split53([1, 1]))          # True
print(split53([1, 1, 1]))       # False
print(split53([2, 4, 2]))       # True
print(split53([5, 3, 2]))       # True
print(split53([5, 3, 2, 1]))    # False