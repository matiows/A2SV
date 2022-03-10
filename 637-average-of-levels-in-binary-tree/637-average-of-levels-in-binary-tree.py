# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        result = []
        
        q = collections.deque()
        
        q.append(root)
        
        while q:
            
            level_nodes = []
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    level_nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            total = 0
            
            for val in level_nodes:
                total += val
            
            if len(level_nodes):
                result.append(total/len(level_nodes))
                
        return result
            
                