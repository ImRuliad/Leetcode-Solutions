#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        do a dfs on p and q
        if curr node in p but curr node not in q -> return False
        if curr node in p and q but node.val in p != node.val in q -> return False
        if entire tree is traversed return True
        '''
        list_p = []
        list_q = []

        def dfs(root, val_list):
            if not root:
                val_list.append(None)
                return
            val_list.append(root.val)
            dfs(root.left, val_list)
            dfs(root.right, val_list)

        dfs(p, list_p)
        dfs(q, list_q)
        return list_p == list_q