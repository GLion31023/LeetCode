def longest_ones(nums: list[int], k: int) -> int:
    left = 0
    max_ones = 0
    count_zeros = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            count_zeros += 1

        while count_zeros > k:
            if nums[left] == 0:
                count_zeros -= 1
            left += 1

        max_ones = max(max_ones, right - left + 1)

    return max_ones


print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(longest_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
print(longest_ones([0, 0, 0, 1], k=4))
