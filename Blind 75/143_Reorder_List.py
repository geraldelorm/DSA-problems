# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        
        #find the middel of the linkedlist
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse the second half of the linkedlist
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #merge the two halves of the linkedlist   
        first, second = head, prev 
        while second.next:
            temp1, temp2 = first.next, second.next 
            first.next = second
            second.next = temp1
            first, second  = temp1, temp2
            
# Time = O(n)
# Space = O(1)