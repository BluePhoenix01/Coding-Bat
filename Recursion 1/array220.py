def array220(nums, idx = 0):
    if idx == len(nums)-1:
        return False
    return True if nums[idx]*10 == nums[idx+1] else array220(nums, idx + 1)

print(array220([1, 2, 20]))
print(array220([1, 2, 30]))
print(array220([2, 20, 2]))