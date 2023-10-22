"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied = Node(0, None, None)
        copiedHead = copied

        #Clone LinkedList with Random pointer poniting to original List
        curr = head
        while curr:
            copiedHead.next = Node(curr.val, None, curr)  #clone val and random -> original
            copiedHead = copiedHead.next
            curr = curr.next


        #Change next poninter in original nodes to clones nodes
        curr = head
        copiedHead = copied.next
        while curr:
            temp = curr.next
            curr.next = copiedHead
            copiedHead = copiedHead.next
            curr = temp


        #change random pointer in cloned to randon->random->next
        copiedHead = copied.next
        while copiedHead:
            copiedHead.random = copiedHead.random.random.next if copiedHead.random.random else None
            copiedHead = copiedHead.next

        return copied.next

        # TC: O(N) 3 N
        # SC: O(N) 
