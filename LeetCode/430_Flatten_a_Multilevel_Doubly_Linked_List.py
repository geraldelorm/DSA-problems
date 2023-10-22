"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

#Creating a new Node for every node I came accross
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = Node(0, None, None, None) 
        self.currHead = newHead

        def flatten_helper(node):

            curr = node
            while curr:
                newNode = Node(curr.val, self.currHead, None, None)
                self.currHead.next = newNode
                self.currHead = self.currHead.next
                if curr.child:
                   flatten_helper(curr.child)
                   #currHead.next.child = None     
                curr = curr.next
                

        flatten_helper(head)

        #detach the dummyHead from the original values starting from its next
        result = newHead.next
        if result: result.prev = None
        return result
# TC: O(N)
# SC: O(N)

#Without creating new Nodes 
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        pseudoHead = Node(0, None, head, None) 

        def flatten_helper(prev, curr):
            if not curr: return prev

            curr.prev = prev
            prev.next = curr

            newCurrNode = curr.next
            newPrevNode = flatten_helper(curr, curr.child)

            curr.child = None
            return flatten_helper(newPrevNode, newCurrNode)

        flatten_helper(pseudoHead, head)

        #detach the dummyHead from the original values starting from its next
        pseudoHead.next.prev = None
        return pseudoHead.next

# tc: O(n)
# sc: O(n)