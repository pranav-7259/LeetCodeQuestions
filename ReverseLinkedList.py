#Create Prev = None, curr = head
#In the loop, keep a variable next_node to keep track of next node ( curr.next )
#Now make curr.next = prev ( break the link to next node and connect it to prevoius node - reverse link )
#Move prev pointer to current
#Move current pointer to next node
#Return previous pointer


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev
        
        
