# Naive Solution
# O(n) Time
# O(n) Space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge case if we are given an empty list
        if not head:
            return True
            
        #store the values of the linked list
        values = []
        cur = head

        #Iterate through linked list and add values to array/list
        while cur:
            values.append(cur.val)
            cur = cur.next
            
        #compare values with its reversed
        return values == values[::-1]


# Optimal SolutionO

# (n) Time
# O(1) Space

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Edge Case
        if not head:
            return True

        #If you have not done Leetcode 876, do that one first
        #Here we use the slow and fast pointer method to find the middle point

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # If you have not dont LeetCode 206, Please do that first
        #Now that we have our mid point (slow pointer) let's reverse it


        prev = None

        # Make sure we do not have cycles in our linked list
        cur = slow.next
        slow.next = None

        while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt


        # Finally check the values of the reversed list and the original list
        left, right = head, prev

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
