def pivot_index(nums: list[int]) -> int:
    total = sum(nums)
    left = 0

    for n in range(len(nums)):
        if left == total - nums[n] - left:
            return n
        left += nums[n]

    return -1


print(pivot_index([1, 7, 3, 6, 5, 6]))
print(pivot_index([1, 2, 3]))
print(pivot_index([2, 1, -1]))
print(pivot_index([1, 2, 3, 4, 6, 0, -6]))
