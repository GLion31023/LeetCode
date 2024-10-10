def max_width_ramp(nums: list[int]) -> int:
    end = len(nums) - 1
    streak = 0
    stack = []

    for i in range(len(nums)):
        if not stack or nums[i] < nums[stack[-1]]:
            stack.append(i)

    for j in range(end, -1, -1):
        while stack and nums[j] >= nums[stack[-1]]:
            i = stack.pop()
            streak = max(streak, j - i)

    return streak


print(max_width_ramp([6, 0, 8, 2, 1, 5]))
print(max_width_ramp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
print(max_width_ramp([2, 2, 1]))
print(max_width_ramp([1, 0]))
print(max_width_ramp([2, 3, 1]))
print(max_width_ramp([2, 4, 3, 1]))

# Example 1:
# Input: nums = [6,0,8,2,1,5]
# Output: 4
# Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.

# Example 2:
# Input: nums = [9,8,1,0,1,9,4,0,4,1]
# Output: 7
# Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
