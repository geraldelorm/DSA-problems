# Using a map
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        map_of_list_one = set()

        curr = headA
        while curr:
            map_of_list_one.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in map_of_list_one:
                return curr
            curr = curr.next
        
        
        return None

# TC: (n + M)
# SC: O(n)


# O(1) space solution
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        pointerA = headA
        pointerB = headB
        while pointerA != pointerB:
            if pointerA == None:
                pointerA = headB
            else:
                pointerA = pointerA.next

            if pointerB == None:
                pointerB = headA
            else:
                pointerB = pointerB.next
        
        return pointerA

# TC: (n + M)
# SC: O(1)