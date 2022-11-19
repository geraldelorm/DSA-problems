# Given the head of a singly linked list, reverse the list, and return the reversed list.
# E.g
# 1 -> 2 -> 3 -> 4 -> None : 4 -> 3 -> 2 -> 1 -> None
# 5 -> None : 5 -> None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Iterative approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

# Time = O(N)
# Space = O(1)


# Recursive approach
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None
        return newHead

# Time = O(N)
# Space = O(N)
