def array_rank_transform(arr: list[int]) -> list[int]:
    # for better runtime performance:
    if not arr:
        return []
    sorted_arr = sorted(set(arr))
    ranks = {sorted_arr[0]: 1}
    rank = 1

    for i in range(1, len(sorted_arr)):
        n = sorted_arr[i]
        rank += 1
        ranks[n] = rank

    return [ranks[n] for n in arr]


# less memory usage:
# def array_rank_transform(arr: list[int]) -> list[int]:
#     if not arr:
#         return []
#     sorted_arr = sorted(arr)
#     ranks = {sorted_arr[0]: 1}
#     rank = 1
#     last = sorted_arr[0]
#
#     for i in range(1, len(sorted_arr)):
#         n = sorted_arr[i]
#         if n != last:
#             rank += 1
#         ranks[n] = rank
#         last = n
#
#     return [ranks[n] for n in arr]

print(array_rank_transform([40, 10, 20, 30]))
print(array_rank_transform([100, 100, 100]))
print(array_rank_transform([37, 12, 28, 9, 100, 56, 80, 5, 12]))

# Example 1:
# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

# Example 2:
# Input: arr = [100,100,100]
# Output: [1,1,1]
# Explanation: Same elements share the same rank.

# Example 3:
# Input: arr = [37,12,28,9,100,56,80,5,12]
# Output: [5,3,4,2,8,6,7,1,3]
