"""
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = float('-inf')

        def get_height(root):
            if root is None:
                return -1

            return 1 + max(get_height(root.left), get_height(root.right))

        def tree_walk(root):
            nonlocal diameter
            if root is None:
                return
            curr_diameter = get_height(root.left) + get_height(root.right) + 2
            diameter = max(diameter, curr_diameter)
            tree_walk(root.left)
            tree_walk(root.right)

        tree_walk(root)
        return diameter