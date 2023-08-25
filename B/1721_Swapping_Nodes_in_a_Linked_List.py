# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        firstNode, endNode, curr = head, head, head
        count = 1

        while curr:
            if count == k:
                firstNode = curr

            #keep endNode k steps behind curr to determine end node
            if count > k:
                endNode =  endNode.next

            count += 1
            curr = curr.next

        
        #swap values 
        firstNode.val, endNode.val = endNode.val, firstNode.val

        return head

# One pass O(N)
# SC : O(1)
