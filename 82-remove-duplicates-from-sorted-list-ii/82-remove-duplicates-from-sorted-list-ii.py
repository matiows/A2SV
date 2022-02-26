# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        listTemp = ListNode()
        start = listTemp
        
        while head and head.next:
            if head.val != head.next.val:
                
                temp = ListNode(head.val)
                listTemp.next = temp
                listTemp = listTemp.next
                head = head.next
            
            else:
                temp = head.val
                
                while head and head.val == temp:
                    head = head.next
        
        if head and not head.next:
            listTemp.next = head
        
        return start.next