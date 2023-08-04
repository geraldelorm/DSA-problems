# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #get to the left position to start the reversal
        newHead = ListNode(0, head)
        prev, curr = newHead, head
        
        while left - 1:
            prev, curr = curr, curr.next
            left -= 1
            right -= 1
        
        left_prev = prev
        
        #reverse from left to right position
        while right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right -= 1
        
        #realign the list ie(node b4 left point to the last reversed node)
        left_prev.next.next = curr
        left_prev.next = prev
        
        return newHead.next
    
    # TC: O(n)
    # SC:O(1)