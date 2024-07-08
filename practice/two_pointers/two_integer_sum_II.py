def two_sum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        if numbers[left] + numbers[right] < target:
            left += 1
        if numbers[left] + numbers[right] > target:
            right -= 1


print(two_sum(numbers=[1, 2, 3, 4], target=3))
print(two_sum(numbers=[2, 3, 5, 8, 11, 13], target=19))
print(two_sum(numbers=[2, 3, 4], target=6))
