# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get to middle 

        if not head or not head.next: return head

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next   

        mid = slow

        # reverse second half 
        prev = None
        curr = mid

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge first half and reversed second half
        first_head, second_head = head, prev

        while second_head.next:
            temp = first_head.next
            first_head.next = second_head
            first_head = temp

            tmp = second_head.next
            second_head.next = first_head
            second_head = tmp

        # TC: O(N)
        # SC: O(1)