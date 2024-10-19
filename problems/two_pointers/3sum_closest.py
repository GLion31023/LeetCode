def three_sum_closest(nums: list[int], target: int) -> int:
    closest = float('inf')
    nums.sort()
    end = len(nums) - 1

    for i in range(end - 1):
        left, right = i + 1, end

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if abs(curr_sum - target) < abs(closest - target):
                closest = curr_sum

            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return curr_sum

    return closest


print(three_sum_closest([-1, 2, 1, -4], target=1))
print(three_sum_closest([0, 0, 0], target=1))
print(three_sum_closest([0, 1, 2], target=3))
print(three_sum_closest([4, 0, 5, -5, 3, 3, 0, -4, -5], target=-2))

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
