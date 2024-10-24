from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


def max_lvl_sum(root: Optional[TreeNode]) -> int:
    q = deque([root])

    max_lvl = curr_lvl = 1
    max_sum = root.val

    while q:
        lvl_len = len(q)
        lvl_sum = 0

        for _ in range(lvl_len):
            n = q.popleft()
            lvl_sum += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        if max_sum < lvl_sum:
            max_sum = lvl_sum
            max_lvl = curr_lvl

        curr_lvl += 1

    return max_lvl


tree = TreeNode(1)
tree.left = TreeNode(7)
tree.left.left = TreeNode(7)
tree.left.right = TreeNode(-8)
tree.right = TreeNode(0)

print(max_lvl_sum(tree))

tree1 = TreeNode(989)
tree1.right = TreeNode(10250)
tree1.right.left = TreeNode(98693)
tree1.right.right = TreeNode(-89388)
tree1.right.right.right = TreeNode(-32127)

print(max_lvl_sum(tree1))

# Example 1:
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation:
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# Example 2:
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
