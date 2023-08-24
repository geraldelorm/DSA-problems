# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr = head

        while curr:
            vals.append(curr.val)
            curr = curr.next

        left, right = 0, len(vals) -1

        while left <= right:
            if vals[left] != vals[right]:
                return False

            left += 1
            right -= 1

        return True

    # TC: O(n)
    # SC: O(n)



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return head

        #get to middle - reverse second half and compare:

    # TC: O(n)
    # SC: O(1)