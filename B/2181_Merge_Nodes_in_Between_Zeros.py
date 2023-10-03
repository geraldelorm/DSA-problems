# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        prev = head
        curr = head.next

        while curr:
            if curr.val == 0:
                if curr.next:
                    prev = prev.next
                    curr = prev.next
                    continue
                else:
                    prev.next = None
                    break
                
            prev.val += curr.val
            prev.next = curr.next

            curr = prev.next

        return head

# TC: O(n)
# SC: O(1)
        