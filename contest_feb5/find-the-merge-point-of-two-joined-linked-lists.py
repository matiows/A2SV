# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    memory = set()
    while head1:
        memory.add(head1)
        head1 = head1.next
    
    while head2:
        if head2 in memory:
            return head2.data
        head2 = head2.next
   