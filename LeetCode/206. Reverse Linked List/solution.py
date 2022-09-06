# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# Iterative Solution
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode, currNode = None, head
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return prevNode

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