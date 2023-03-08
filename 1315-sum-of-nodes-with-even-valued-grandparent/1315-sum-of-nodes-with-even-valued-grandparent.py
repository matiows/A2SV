# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def traverse(node,parent,grand):
            if not node:
                return 0
            
            left = traverse(node.left, node.val, parent)
            right = traverse(node.right, node.val, parent)
            
            ans = left + right
            
            if grand and grand % 2 == 0:
                ans += node.val 
            
            return ans
        
        res = traverse(root, None, None)
        
        return res