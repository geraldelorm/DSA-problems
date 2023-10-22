# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        first, second = head, head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second

# TC: O(N)
# SC: O(N)

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        dummy = ListNode(0)
        dummy.next = head

        prev, curr = dummy, head
        while curr and curr.next:
            first = curr
            second = curr.next

            prev.next = second
            first.next = second.next
            second.next = first
            

            prev = first
            curr = curr.next

        return dummy.next

# TC: O(N)
# SC: O(1)