import heapq
from math import ceil


def max_k_elements(nums: list[int], k: int) -> int:
    score = 0

    max_heap = [-n for n in nums]
    heapq.heapify(max_heap)

    for _ in range(k):
        curr_max = -heapq.heappop(max_heap)
        score += curr_max

        new_val = ceil(curr_max / 3)
        heapq.heappush(max_heap, -new_val)

    return score


print(max_k_elements([10, 10, 10, 10, 10], k=5))
print(max_k_elements([1, 10, 3, 3, 3], k=3))

# Example 1:
#
# Input: nums = [10,10,10,10,10], k = 5
# Output: 50
# Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.

# Example 2:
# Input: nums = [1,10,3,3,3], k = 3
# Output: 17
# Explanation: You can do the following operations:
# Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
# Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
# Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
# The final score is 10 + 4 + 3 = 17.
