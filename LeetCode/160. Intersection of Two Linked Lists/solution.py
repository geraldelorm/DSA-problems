# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_of_A, len_of_B = 0, 0
        currA, currB = headA, headB

        while currA is not None:
            len_of_A += 1
            currA = currA.next

        while currB is not None:
            len_of_B += 1
            currB = currB.next

        diff = abs(len_of_A - len_of_B)

        if len_of_A > len_of_B:
            for i in range(diff):
                headA = headA.next

        elif len_of_B > len_of_A:
            for i in range(diff):
                headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA

# O(M + N)


# Using stacks
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stack_of_A, stack_of_B = deque(), deque()

        while headA is not None:
            stack_of_A.append(headA)
            headA = headA.next

        while headB is not None:
            stack_of_B.append(headB)
            headB = headB.next

        intersection = None

        while stack_of_A and stack_of_B:
            nodeA, nodeB = stack_of_A.pop(), stack_of_B.pop()
            if nodeA == nodeB:
                intersection = nodeA

        return intersection
# O(M+N) space
