"""
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        result: list[str] = []

        def preorder(node, path):
            if not node:
                return
            path += str(node.val)

            if node.left is None and node.right is None:
                result.append(path)
            else:
                path += "->"
                preorder(node.left, path)
                preorder(node.right, path)
        preorder(root, "")
        return result