from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val} -> left {self.left} -> right {self.right}"


def longest_zigzag_path(root: Optional[TreeNode]) -> int:
    stack = [[root, None, 0]]
    longest_path = 0

    while stack:
        node, last_dir, count = stack.pop()
        longest_path = max(longest_path, count)
        if node.left:
            if not last_dir or last_dir == 'left':
                stack.append([node.left, 'left', 1])
            else:
                stack.append([node.left, 'left', count + 1])
        if node.right:
            if not last_dir or last_dir == 'right':
                stack.append([node.right, 'right', 1])
            else:
                stack.append([node.right, 'right', count + 1])

    return longest_path


tree = TreeNode(1)
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)
tree.right.right = TreeNode(3)
tree.right.right.left = TreeNode(4)
tree.right.right.right = TreeNode(4)
tree.right.right.left.right = TreeNode(5)
tree.right.right.left.right.right = TreeNode(6)

print(longest_zigzag_path(tree))


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(2)
tree1.left.right = TreeNode(3)
tree1.left.right.left = TreeNode(4)
tree1.left.right.right = TreeNode(4)
tree1.left.right.left.right = TreeNode(5)

print(longest_zigzag_path(tree1))

# Example 1:
# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

# Example 2:
# Input: root = [1,1,1,null,1,null,null,1,1,null,1]
# Output: 4
# Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).

# Example 3:
# Input: root = [1]
# Output: 0
