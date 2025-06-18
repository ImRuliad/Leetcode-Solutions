"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        inorder_list: list[int] = []

        def inorder(node):
            if node:
                inorder(node.left)
                inorder_list.append(node.val)
                inorder(node.right)

        inorder(root)
        return inorder_list