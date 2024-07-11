def find_max_average(nums: list[int], k: int) -> float:
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


print(find_max_average([1, 12, -5, -6, 50, 3], k=4))
print(find_max_average([5], k=1))
print(find_max_average([-1], k=1))
