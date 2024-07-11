from collections import defaultdict


def max_operations(nums: list[int], k: int) -> int:
    count = defaultdict(int)
    total = 0

    for num in nums:
        diff = k - num
        if count[diff] > 0:
            total += 1
            count[diff] -= 1
        else:
            count[num] += 1

    return total


print(max_operations([1, 2, 3, 4], k=5))
print(max_operations([3, 1, 3, 4, 3], k=6))
print(max_operations([2, 2, 2, 3, 1, 1, 4, 1], k=4))
print(max_operations([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], k=3))
