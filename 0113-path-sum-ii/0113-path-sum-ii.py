# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node, path, pathSum):
            if not node:
                return
            
            path.append(node.val)
            pathSum += node.val
            
            if not node.right and not node.left and pathSum == targetSum:
                result.append(path)
            
            dfs(node.left, path.copy(), pathSum)
            dfs(node.right, path.copy(), pathSum)
         
        dfs(root, [], 0)  
        return result
        