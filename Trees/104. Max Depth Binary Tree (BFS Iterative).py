"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is:
    the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = ([root])
        depth = 0

        while queue:
            queue_size = len(queue)

            for _ in range(queue_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth