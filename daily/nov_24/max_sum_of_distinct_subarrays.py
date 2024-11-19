from collections import Counter


def max_subarray_sum(nums: list[int], k: int) -> int:
    n = len(nums)
    if n < k:
        return 0

    window_sum = sum(nums[:k])
    window_count = Counter(nums[:k])

    result = window_sum if len(window_count) == k else 0

    for i in range(k, n):
        going = nums[i - k]
        window_count[going] -= 1

        if window_count[going] == 0:
            del window_count[going]

        coming = nums[i]
        window_count[coming] += 1

        window_sum += coming - going

        if len(window_count) == k:
            result = max(window_sum, result)

    return result


print(max_subarray_sum([1, 5, 4, 2, 9, 9, 9], k=3))
print(max_subarray_sum([4, 4, 4], k=3))
print(max_subarray_sum([9, 9, 9, 1, 2, 3], k=3))
print(max_subarray_sum([5, 3, 3, 1, 1], k=3))
print(max_subarray_sum([1, 1, 2], k=2))

# Example 1:
# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

# Example 2:
#
# Input: nums = [4,4,4], k = 3
# Output: 0
# Explanation: The subarrays of nums with length 3 are:
# - [4,4,4] which does not meet the requirements because the element 4 is repeated.
# We return 0 because no subarrays meet the conditions.

# and nums[i - k - 1] != nums[i]
