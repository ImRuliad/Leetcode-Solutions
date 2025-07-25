"""
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, curr_counter):
            if not root:
                return False

            curr_counter += root.val
            if not root.left and not root.right and curr_counter == targetSum:
                return True

            return dfs(root.left, curr_counter) or dfs(root.right, curr_counter)

        return dfs(root, 0)