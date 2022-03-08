# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSym(node1: Optional[TreeNode] , node2: Optional[TreeNode]):
            
            if not node1 and not node2:
                return True 
            
            if not node1 or not node2:
                return False

            return isSym(node1.left , node2.right) and isSym(node2.left , node1.right) and node1.val == node2.val
        
        
        return isSym(root.left , root.right)