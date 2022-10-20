# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0
            
            if not node.left and not node.right:
                return node.val, 0
            
            left, left_child = dfs(node.left)
            right, right_child = dfs(node.right)
            child_sum = left_child + right_child
            my_sum = left + right
            left_right_child = left + right_child
            right_left_child = right + left_child
            maximum_childs = max(left_right_child, right_left_child, child_sum, my_sum)
            
            return node.val + child_sum, maximum_childs
        
        left, right = dfs(root)
        answer = max(left, right)
        return answer