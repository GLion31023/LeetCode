from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} left -> {self.left} ==> {self.val} right -> {self.right} |"


def delete_node_bst(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return root

    if key > root.val:
        root.right = delete_node_bst(root.right, key)
    elif key < root.val:
        root.left = delete_node_bst(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        curr = root.right
        while curr.left:
            curr = curr.left
        root.val = curr.val
        root.right = delete_node_bst(root.right, root.val)

    return root


tree = TreeNode(5)
tree.left = TreeNode(3)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.right = TreeNode(6)
tree.right.right = TreeNode(7)

print(delete_node_bst(tree, 3))


tree1 = TreeNode(5)
tree1.left = TreeNode(2)
tree1.left.right = TreeNode(4)
tree1.right = TreeNode(6)
tree1.right.right = TreeNode(7)

print(delete_node_bst(tree1, 0))

print(delete_node_bst([], 0))

# Example 1:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
#
# Example 2:
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.

# Example 3:
# Input: root = [], key = 0
# Output: []
