# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray of 1's is [1,1,1,1,1].


def longest_subarray(nums: list[int]) -> int:
    max_len = 0
    zeros = 0
    start = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1

        while zeros > 1:
            if nums[start] == 0:
                zeros -= 1
            start += 1

        max_len = max(max_len, i - start)

    return max_len


print(longest_subarray([1, 1, 0, 1]))
print(longest_subarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(longest_subarray([1, 1, 1]))
print(longest_subarray([1, 1, 0, 0, 1, 1, 1, 0, 1]))
print(longest_subarray([0, 0, 1, 1]))
print(longest_subarray([0, 1, 1, 1, 0, 1, 1]))
