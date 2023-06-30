# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two pass solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length of the list
        dummy = ListNode()
        dummy.next = head
        
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        #delete the length - nth node
        length -= n
        
        curr = dummy
        while length > 0:
            length -= 1
            curr = curr.next
            
        curr.next = curr.next.next
        
        return dummy.next
# Time = O(n)
# Space = O(1)
        
    
# One pass solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        while n >= 0:
            second = second.next
            n -= 1      
        
        while second:
            first = first.next
            second = second.next
            
        first.next = first.next.next

        return dummy.next
    
# Time = O(n)
# Space = O(1)