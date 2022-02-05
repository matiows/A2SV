# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        count = 0
        
        while head:
            head = head.next
            count+=1
        
        if count == n:
            return temp.next
        
        head = temp
        
        for _ in range(count-n-1):
            temp = temp.next
         
        temp.next = temp.next.next
        
        return head