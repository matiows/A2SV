# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node, count):
            if not node:
                return
            
            nonlocal answer
            
            left, right = 0, 0
            
            if node.left:
                if node.left.val == node.val:
                    left = dfs(node.left, count + 1)
                else:
                    dfs(node.left, 0)
            if node.right:
                if node.right.val == node.val:
                    right = dfs(node.right, count + 1)
                else:
                    dfs(node.right, 0)

            answer = max(answer, left + right)
            return max(left, right) + 1

        dfs(root, 0)
        return answer