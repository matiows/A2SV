# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_list = []
        
        def dfs(root):
            if root:
                dfs(root.left)
                
                node_list.append(root.val)
                
                dfs(root.right)

        dfs(root)
        
        return node_list[k - 1]
        