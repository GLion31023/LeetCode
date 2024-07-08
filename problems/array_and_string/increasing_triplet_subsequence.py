def increasing_triplet(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False

    smallest = medium = float("inf")

    for n in nums:
        if n <= smallest:
            smallest = n
        elif n <= medium:
            medium = n
        else:
            return True

    return False


print(increasing_triplet([1, 2, 3, 4, 5]))
print(increasing_triplet([5, 4, 3, 2, 1]))
print(increasing_triplet([2, 1, 5, 0, 4, 6]))
print(increasing_triplet([20, 100, 10, 12, 5, 13]))
