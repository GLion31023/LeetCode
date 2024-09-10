# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: Optional[TreeNode], target_sum: int) -> int:
    paths = defaultdict(int)
    paths[0] = 1

    def dfs(node: TreeNode, total: int) -> int:
        count = 0
        if node:
            total += node.val

            count = paths[total - target_sum]

            paths[total] += 1
            count += dfs(node.left, total) + dfs(node.right, total)
            paths[total] -= 1

        return count

    return dfs(root, 0)


# Example 1:
#
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.

# Example 2:
#
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
