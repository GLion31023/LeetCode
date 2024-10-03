def min_subarray(nums: list[int], p: int) -> int:
    total = sum(nums)
    rem = total % p

    if not rem:
        return 0

    res = len(nums)
    cur_sum = 0
    idx_of_rem = {0: -1}

    for i, n in enumerate(nums):
        cur_sum = (cur_sum + n) % p
        prefix = (cur_sum - rem + p) % p
        if prefix in idx_of_rem:
            length = i - idx_of_rem[prefix]
            res = min(res, length)

        idx_of_rem[cur_sum] = i

    return -1 if res == len(nums) else res


print(min_subarray([3, 1, 4, 2], p=6))
print(min_subarray([6, 3, 5, 2], p=9))
print(min_subarray([1, 2, 3], p=3))

# Example 1:
# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by 6.
# We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.

# Example 2:
# Input: nums = [6,3,5,2], p = 9
# Output: 2
# Explanation: We cannot remove a single element to get a sum divisible by 9.
# The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

# Example 3:
# Input: nums = [1,2,3], p = 3
# Output: 0
# Explanation: Here the sum is 6. which is already divisible by 3.
# Thus, we do not need to remove anything.
