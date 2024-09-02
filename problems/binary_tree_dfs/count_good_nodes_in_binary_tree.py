class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root: TreeNode) -> int:
    def dfs(node: TreeNode, path_max: int) -> int:
        if not node:
            return 0

        good = 1 if node.val >= path_max else 0

        path_max = max(path_max, node.val)

        good += dfs(node.left, path_max)
        good += dfs(node.right, path_max)

        return good

    return dfs(root, root.val)


root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.left = TreeNode(3)
root1.right.left = TreeNode(1)
root1.right.right = TreeNode(5)
print(good_nodes(root1))  # Output: 4

# Example 2:
root2 = TreeNode(3)
root2.left = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(2)
print(good_nodes(root2))  # Output: 3

# Example 3:
root3 = TreeNode(1)
print(good_nodes(root3))  # Output: 1
