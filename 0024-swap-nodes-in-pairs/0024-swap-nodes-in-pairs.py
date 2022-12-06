# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr and curr.next:
            nexxt = curr.next
            
            if prev:
                prev.next = nexxt
            else:
                head = nexxt
                
            curr.next = nexxt.next
            nexxt.next = curr
            
            prev = curr
            curr = curr.next
            
        return head