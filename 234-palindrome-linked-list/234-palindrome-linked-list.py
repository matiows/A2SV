# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        Stack = []
        slow = fast = head

        while fast and fast.next:
            Stack.append(slow.val)

            fast = fast.next.next
            slow = slow.next
            
        if fast:
            slow = slow.next
        
        while slow:
            if not slow.val == Stack.pop():
                return False
            
            else:
                slow = slow.next
        
        return True