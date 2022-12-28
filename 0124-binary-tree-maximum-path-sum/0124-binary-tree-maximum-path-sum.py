# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, result):
        if not node:
            return 0
        
        left = self.dfs(node.left, result)
        right = self.dfs(node.right, result)
        
        me_left = left + node.val
        me_right = right + node.val
        answer = max(me_left, me_right, node.val)
        result[0] = max(result[0], answer, me_left + right)
        
        return answer
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [-inf]
        
        self.dfs(root, result)
    
        return result[0]
        