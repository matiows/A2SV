# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        answer = [0]
        
        def find(node):
            if not node:
                return 0
            
            left = find(node.left)
            right = find(node.right)
            
            result = left + right - 1 + node.val
            
            answer[0] += abs(result)
            
            return result 
        
        find(root)
        return answer[0]