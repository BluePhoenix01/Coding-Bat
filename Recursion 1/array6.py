def array6(nums, idx = 0):
    if idx == len(nums):
        return False
    if nums[idx] == 6:
        return True
    return array6(nums, idx + 1)

print(array6([1, 2, 6]))
print(array6([1, 2, 3]))
print(array6([6, 2, 3]))