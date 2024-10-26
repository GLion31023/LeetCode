import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    res = float('-inf')

    max_q = [-n for n in nums]
    heapq.heapify(max_q)

    for i in range(k):
        max_n = -heapq.heappop(max_q)
        if i + 1 == k:
            res = max_n

    return res


print(find_kth_largest(nums=[3, 2, 1, 5, 6, 4], k=2))
print(find_kth_largest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
