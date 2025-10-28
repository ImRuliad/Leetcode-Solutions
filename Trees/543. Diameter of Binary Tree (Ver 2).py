"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = [0]

        def dfs(root, max_d):
            if not root:    return 0
            left = dfs(root.left, max_d)
            right = dfs(root.right, max_d)

            curr_d = left + right
            max_d[0] = max(max_d[0], curr_d)

            return 1 + max(left, right)

        dfs(root, max_d)
        return max_d[0]

