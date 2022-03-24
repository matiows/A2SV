# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        ans = []
        
        if not root:
            return []
        
        while queue:
            temp = [x.val for x in queue]
            ans.append(max(temp))
            for i in range(len(queue)):
                node = queue.popleft()
            
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
        return ans