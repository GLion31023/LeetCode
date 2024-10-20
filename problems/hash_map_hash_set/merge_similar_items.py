from collections import defaultdict


def merge_similar_items(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    merge = defaultdict(int)

    for i in items1:
        w, h = i[0], i[1]
        merge[w] = h

    for i in items2:
        w, h = i[0], i[1]
        merge[w] += h

    result = []

    for k, v in merge.items():
        merged = [k, v]
        result.append(merged)

    result.sort(key=lambda x: x[0])

    return result


print(merge_similar_items(items1=[[1, 1], [4, 5], [3, 8]], items2=[[3, 1], [1, 5]]))
print(merge_similar_items(items1=[[1, 1], [3, 2], [2, 3]], items2=[[2, 1], [3, 2], [1, 3]]))

# Example 1:
# Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
# Output: [[1,6],[3,9],[4,5]]
# Explanation:
# The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
# The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
# The item with value = 4 occurs in items1 with weight = 5, total weight = 5.
# Therefore, we return [[1,6],[3,9],[4,5]].

# Example 2:
# Input: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
# Output: [[1,4],[2,4],[3,4]]
# Explanation:
# The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 3, total weight = 1 + 3 = 4.
# The item with value = 2 occurs in items1 with weight = 3 and in items2 with weight = 1, total weight = 3 + 1 = 4.
# The item with value = 3 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
# Therefore, we return [[1,4],[2,4],[3,4]].
