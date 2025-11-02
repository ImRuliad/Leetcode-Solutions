"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node: Optional[TreeNode], out: List[int]) -> None:
        if not node:
            return
        out.append(node.val)
        self.dfs(node.left, out)
        self.dfs(node.right, out)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        return res