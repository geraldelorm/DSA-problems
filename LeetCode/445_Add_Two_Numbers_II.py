# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            _nxt = curr.next
            curr.next = prev
            prev = curr
            curr = _nxt

        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #reverse both lists 
        head1 = self.reverseList(l1)
        head2 = self.reverseList(l2)

        #add the two lists
        addedList = self.addTwoReversedNumbers(head1, head2)

        #revese the result list
        return self.reverseList(addedList)

    def addTwoReversedNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result
        carry = 0

        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            carry, _sum = divmod(carry + l1Val + l2Val, 10)

            result.next = ListNode(_sum)

            result = result.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next

# TC: O(n)
# SC: O(n)


#Using a stack
class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            _nxt = curr.next
            curr.next = prev
            prev = curr
            curr = _nxt

        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []

        curr1, curr2 = l1, l2

        while curr1 or curr2:
            if curr1:
                s1.append(curr1.val)
                curr1 = curr1.next

            if curr2:
                s2.append(curr2.val)
                curr2 = curr2.next

        resList = ListNode()
        curr, carry = resList, 0

        while s1 or s2 or carry:
            v1 = s1.pop() if s1 else 0
            v2 = s2.pop() if s2 else 0

            total = v1 + v2 + carry

            carry, _sum = divmod(total, 10)
            curr.next = ListNode(_sum)
            
            curr = curr.next

        return self.reverseList(resList.next)

# TC: O(N)
# SC: O(N)
