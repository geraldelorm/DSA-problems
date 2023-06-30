# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Brute Force
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
                
        curr = head = ListNode(0)
        for v in sorted(nodes):
            curr.next = ListNode(v)
            curr = curr.next
            
        return head.next
    
# Time = O(nlogn) where n == total number of nodes in all the linkedlist in the list
# Space = O(n) => storing node sin an array

# Efficient Solution - Merge Two list at a time with divide and conque
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0: return None
        
        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i < len(lists) - 1 else None
                
                mergedList.append(self.mergeLists(l1, l2))
                
            lists = mergedList
        return lists[0]
    
    
    def mergeLists(self, l1, l2):
        head = ListNode()
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
            
        return head.next
       
# Time = O(nlogk) k = no. of linkedlists n = no. of nodes
# Space = O(1)