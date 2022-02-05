# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node_idx = self.removeNode(head, n)
        
        if node_idx == n:
            return head.next
        
        return head
    
    def removeNode (self, node, n):
        if not node:
            return 0
        
        node_idx = self.removeNode(node.next, n)
        
        if node_idx == n:
            node.next = node.next.next
        
        return node_idx+1
        