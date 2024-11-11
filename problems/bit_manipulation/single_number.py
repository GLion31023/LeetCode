from collections import defaultdict


def single_num(nums: list[int]) -> int:
    seen = defaultdict(int)

    for n in nums:
        seen[n] += 1

    for k, v in seen.items():
        if v == 1:
            return k


print(single_num([2, 2, 1]))
print(single_num([4, 1, 2, 1, 2]))
print(single_num([1]))

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1
