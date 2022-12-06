# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr and curr.next:
            nextt = curr.next
            curr.next = nextt.next
            nextt.next = curr
            
            if prev:
                prev.next = nextt
            else:
                head = nextt
                
            prev = curr
            curr = curr.next
        
        return head