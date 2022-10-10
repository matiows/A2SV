# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        glob = 0
        
        def dfs(gpar, par, ch):
            
            if not ch:
                return
            
            nonlocal glob
            
            if gpar and gpar.val % 2 == 0:
                glob+=ch.val
            
            dfs(par,ch,ch.left)
            dfs(par,ch,ch.right)
            
        dfs(None, None, root)
        return glob