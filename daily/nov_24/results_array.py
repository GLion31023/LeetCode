def results_array(nums, k):
    window = nums
    if k == 1:
        return window

    l, r = 0, 0

    while r < (len(window) - 1):
        if window[r] + 1 == window[r + 1]:
            r += 1
            if r - l == k - 1:
                window[l] = window[r]
                l += 1

        elif window[r] + 1 != window[r + 1]:
            while l <= r:
                window[l] = -1
                l += 1

            r += 1

    return window[:len(window) - k + 1]


print(results_array([1, 2, 3, 4, 3, 2, 5], k=3))
print(results_array([2, 2, 2, 2, 2], k=4))
print(results_array([3, 2, 3, 2, 3, 2], k=2))
print(results_array([1], k=1))

# Example 1:
#
# Input: nums = [1,2,3,4,3,2,5], k = 3
# Output: [3,4,-1,-1,-1]
# Explanation:
# There are 5 subarrays of nums of size 3:
# [1, 2, 3] with the maximum element 3.
# [2, 3, 4] with the maximum element 4.
# [3, 4, 3] whose elements are not consecutive.
# [4, 3, 2] whose elements are not sorted.
# [3, 2, 5] whose elements are not consecutive.

# Example 2:
# Input: nums = [2,2,2,2,2], k = 4
# Output: [-1,-1]

# Example 3:
# Input: nums = [3,2,3,2,3,2], k = 2
# Output: [-1,3,-1,3,-1]
