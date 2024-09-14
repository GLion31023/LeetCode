def longest_subarray(nums: list[int]) -> int:
    result = 0
    streak = 0
    maxi = max(nums)

    for n in nums:
        if n == maxi:
            streak += 1
            result = max(result, streak)
        else:
            streak = 0

    return result


print(longest_subarray([1, 2, 3, 3, 2, 2]))
print(longest_subarray([1, 2, 3, 4]))
print(longest_subarray([100, 5, 5]))
print(longest_subarray([96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 279979]))
