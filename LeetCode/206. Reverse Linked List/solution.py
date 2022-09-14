# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None

        while head:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode

        return prevNode
# Time = O(n)
# Space = O(1)

# Time Complexity = O(n)
# Space Complexity = O(1)
    
# Recursive Solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead  = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead

# Time Complexity = O(n)
# Space Complexity = O(n)