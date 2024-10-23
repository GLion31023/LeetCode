from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


def right_side_view(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []

    q = deque()
    q.append(root)

    result = []

    while q:
        q_len = len(q)
        curr_lvl = None
        for _ in range(q_len):
            v = q.popleft()
            curr_lvl = v.val
            if v.left:
                q.append(v.left)
            if v.right:
                q.append(v.right)

        result.append(curr_lvl)

    return result


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(4)

print(right_side_view(tree))

# Example 1:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]

# Example 3:
# Input: root = []
# Output: []
