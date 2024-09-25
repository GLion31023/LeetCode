def search_insert(nums: list[int], target: int) -> int:
    s, e = 0, len(nums) - 1

    while s <= e:
        mid = (s + e) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            s = mid + 1
        else:
            e = mid - 1
    return s


print(search_insert(nums=[1, 3, 5, 6], target=5))
print(search_insert(nums=[1, 3, 5, 6], target=2))
print(search_insert(nums=[1, 3, 5, 6], target=7))
print(search_insert(nums=[1, 3, 5, 6, 9, 15, 25, 44, 50], target=7))

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
