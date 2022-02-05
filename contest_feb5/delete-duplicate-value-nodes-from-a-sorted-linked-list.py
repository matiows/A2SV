#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    head = llist
    
    while llist and llist.next:
        
        while llist.next and (llist.data == llist.next.data):
            
            llist.next = llist.next.next
        
        llist = llist.next
    
    return head
    