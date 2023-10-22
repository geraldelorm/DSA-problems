# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        return prev
    
# Time = O(n)
# Space = O(1)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head    

        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
            
        return prev
    
# Time = O(n)
# Space = O(n)