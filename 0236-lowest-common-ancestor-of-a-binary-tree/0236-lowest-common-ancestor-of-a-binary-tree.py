# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = None 
        
        def dfs(node):
            nonlocal ancestor
            if not node:
                return False
            
            if node == p or node == q:
                ancestor = node
                return True
                
            left = dfs(node.left) if node.left else False
            right = dfs(node.right) if node.right else False
            
            if left and right:
                ancestor = node
                return True
            
            return left or right
        
        dfs(node)
        return ancestor
                