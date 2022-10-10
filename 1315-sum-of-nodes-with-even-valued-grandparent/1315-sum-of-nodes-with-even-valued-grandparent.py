# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        total = 0
        def dfs(gpar, par):
            
            if not par:
                return
            
            nonlocal total
            
            if gpar and gpar.val % 2 == 0:
                if par.left:
                    total+=par.left.val
                if par.right:
                    total+=par.right.val
            
            dfs(par,par.left)
            dfs(par,par.right)
            
        dfs(None, root)
        return total