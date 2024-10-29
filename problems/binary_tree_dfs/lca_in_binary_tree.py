from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> left {self.left} -> right {self.right} ||"


def lca(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> TreeNode:
    if not root or root == p or root == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    return left if left else right


tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
tree.left.left = TreeNode(6)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(7)
tree.left.right.right = TreeNode(4)
tree.right.left = TreeNode(0)
tree.right.right = TreeNode(8)

x = tree.left
y = tree.right

print(lca(tree, x, y))

tree1 = TreeNode(3)
tree1.left = TreeNode(5)
tree1.left.left = TreeNode(6)
tree1.left.right = TreeNode(2)
tree1.left.right.left = TreeNode(7)
tree1.left.right.right = TreeNode(4)
tree1.right = TreeNode(1)
tree1.right.left = TreeNode(0)
tree1.right.right = TreeNode(8)
x1 = tree1.left
y1 = tree1.left.right.right

print(lca(tree1, x1, y1))

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.left.right = TreeNode(4)
tree2.right = TreeNode(3)
x2 = tree2.left.right
y2 = tree2.right

print(lca(tree2, x2, y2))

tree3 = TreeNode(-1)
tree3.left = TreeNode(0)
tree3.left.left = TreeNode(-2)
tree3.left.left.left = TreeNode(8)
tree3.left.right = TreeNode(4)
tree3.right = TreeNode(3)
x3 = tree3.right
y3 = tree3.left.left.left

print(lca(tree3, x3, y3))

# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1
