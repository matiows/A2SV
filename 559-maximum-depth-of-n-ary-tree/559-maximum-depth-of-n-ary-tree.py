"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        
        if len(root.children) == 0:
            return 1

        max_depth = 0

        for i in range(len(root.children)):

            depth = self.maxDepth(root.children[i])

            max_depth = max(depth, max_depth)

        return max_depth+1