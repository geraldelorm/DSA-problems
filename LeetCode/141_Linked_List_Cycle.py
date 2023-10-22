# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

# Time Complexity = O(n)
# Space Complexity = O(1)


# Using a hash set
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        lookup = set()
        while head:
            if head in lookup:
                return True
            lookup.add(head)
            head = head.next
        return False

# Time Complexity = O(n)
# Space Complexity = O(n) space of the set