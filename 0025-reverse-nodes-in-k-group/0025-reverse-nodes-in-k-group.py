# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        last: Optional[ListNode] = head
        first: Optional[ListNode] = head
        steps = 1
        
        while steps < k:
            if last == None:
                return head
            last = last.next
            steps += 1
            
        if last == None:
            return head
			
        head = last
		
        self.reverse(first,last).next = self.reverseKGroup(last.next,k)
		
        return head 
            
    def reverse(self,first: Optional[ListNode],last: Optional[ListNode]):
        prev: Optional[ListNode] = None
        current: Optional[ListNode] = first
        last: Optional[ListNode] = last.next
        temp: Optional[ListNode]
            
        while (current != last):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return first