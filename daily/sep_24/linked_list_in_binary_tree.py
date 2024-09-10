from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_sub_path(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

    def dfs(head, node):
        if not head:
            return True
        if not node or head.val != node.val:
            return False
        return dfs(head.next, node.left) or dfs(head.next, node.right)

    def traverse(head, node):
        if not node:
            return False
        if dfs(head, node):
            return True
        return traverse(head, node.left) or traverse(head, node.right)

    return traverse(head, root)
