# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLeaves(self, root: Optional[TreeNode]) -> list[int]:
        leaves = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if not node.left and not node.right:
                    leaves.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return leaves

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)
