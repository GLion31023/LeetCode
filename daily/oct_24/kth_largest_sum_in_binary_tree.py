from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_largest_level_sum(root: Optional[TreeNode], k: int) -> int:
    result = []

    q = deque()
    q.append(root)

    while any(q):
        q_len = len(q)
        level_res = 0
        for n in range(q_len):
            node = q.popleft()
            if node:
                level_res += node.val
                q.append(node.left)
                q.append(node.right)
        result.append(level_res)

    result.sort(reverse=True)

    if 0 <= k - 1 <= len(result) - 1:
        return result[k - 1]
    else:
        return -1


tree = TreeNode(5)
tree.left = TreeNode(8)
tree.right = TreeNode(9)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(1)
tree.left.left.left = TreeNode(4)
tree.left.left.right = TreeNode(6)
tree.right.left = TreeNode(3)
tree.right.right = TreeNode(7)

print(kth_largest_level_sum(tree, 2))


# Example 1:
# Input: root = [5,8,9,2,1,3,7,4,6], k = 2
# Output: 13
# Explanation: The level sums are the following:
# - Level 1: 5.
# - Level 2: 8 + 9 = 17.
# - Level 3: 2 + 1 + 3 + 7 = 13.
# - Level 4: 4 + 6 = 10.
# The 2nd largest level sum is 13.

# Example 2:
# Input: root = [1,2,null,3], k = 1
# Output: 3
# Explanation: The largest level sum is 3.
