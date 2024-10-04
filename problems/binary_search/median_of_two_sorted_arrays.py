def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2

    l, r = 0, m
    while l <= r:
        a = (l + r) // 2
        b = half - a

        n1_left_max = nums1[a - 1] if a > 0 else float('-inf')
        n1_right_min = nums1[a] if a < m else float('inf')
        n2_left_max = nums2[b - 1] if b > 0 else float('-inf')
        n2_right_min = nums2[b] if b < n else float('inf')

        if n1_left_max <= n2_right_min and n2_left_max <= n1_right_min:
            if total % 2 == 1:
                return min(n1_right_min, n2_right_min)
            return (max(n1_left_max, n2_left_max) + min(n1_right_min, n2_right_min)) / 2
        elif n1_left_max > n2_right_min:
            r = a - 1
        else:
            l = a + 1

    # sorted_nums = sorted(nums1 + nums2)
    # length = len(sorted_nums)
    #
    # if length % 2 == 1:
    #     return sorted_nums[length // 2]
    # else:
    #     a = sorted_nums[length // 2]
    #     b = sorted_nums[(length // 2) - 1]
    #     return (a + b) / 2


print(find_median_sorted_arrays([1, 3], nums2=[2]))
print(find_median_sorted_arrays([1, 2], nums2=[3, 4]))

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
