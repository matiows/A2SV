# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)

        flag = 1
        result = []        
        while q:
            
            level_nodes = []
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    level_nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if flag % 2 == 0 and len(level_nodes):
                result.append(level_nodes[::-1])
            elif len(level_nodes):
                result.append(level_nodes)
                
            flag += 1
        return result