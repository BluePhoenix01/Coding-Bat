def array11(nums, idx = 0):
    if idx == len(nums):
        return False
    return int(nums[idx] == 11) + array11(nums, idx + 1)

print(array11([1, 2, 11]))
print(array11([1, 11, 11]))
print(array11([11, 11, 11])) 