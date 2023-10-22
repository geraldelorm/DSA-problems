# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
            
        return False
    
#  Time = O(n)
#  Space = O(n)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
            
        return False
    
#  Time = O(n)
#  Space = O(1)
        