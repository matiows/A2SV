# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        target = TreeNode(val)
        if not root:
            return target
        def insert(node):
            if node.val < val:
                if node.right:
                    insert(node.right)
                else:
                    node.right = target
            else:
                if node.left:
                    insert(node.left)
                else:
                    node.left = target
        insert(root)
        return root