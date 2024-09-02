from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_leaves(root: Optional[TreeNode]) -> list[int]:
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


def leaf_similar(first_root: Optional[TreeNode], second_root: Optional[TreeNode]) -> bool:
    return get_leaves(first_root) == get_leaves(second_root)


root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

print(leaf_similar(root1, root2))


root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)

root4 = TreeNode(1)
root4.left = TreeNode(3)
root4.right = TreeNode(2)

print(leaf_similar(root3, root4))
