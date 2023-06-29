# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Working Solution - Not very clean
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res =  ListNode()
        currRes = res
        remainder = 0

        while l1 and l2:
            curr_total = l1.val + l2.val + remainder
            remainder = curr_total // 10
            currRes.next = ListNode(curr_total % 10)
            currRes = currRes.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            curr_total = l1.val + remainder
            remainder = curr_total // 10
            currRes.next = ListNode(curr_total % 10)
            currRes = currRes.next
            l1 = l1.next
            
        while l2:
            curr_total = l2.val + remainder
            remainder = curr_total // 10
            currRes.next = ListNode(curr_total % 10)
            currRes = currRes.next
            l2 = l2.next
            
        if remainder != 0:
            currRes.next = ListNode(remainder)
            currRes = currRes.next
            
        return res.next
            
# Time = O(max(n, m) + 1)
# Space = O(max(n, m) + 1)



# Clean Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res =  ListNode()
        currRes = res
        remainder = 0

        while l1 or l2 or remainder:
            curr_total = remainder
            if l1:
                curr_total += l1.val
                l1 = l1.next   
            if l2:
                curr_total += l2.val
                l2 = l2.next
                
            remainder = curr_total // 10
            val = curr_total % 10
            currRes.next = ListNode(val)
            currRes = currRes.next
            
        return res.next
  
 
# # Time = O(max(n, m) + 1)
# Space = O(max(n, m) + 1)     