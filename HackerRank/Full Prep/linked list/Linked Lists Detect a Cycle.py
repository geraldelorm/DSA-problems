"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    #     seen = set()

    #     while head:
    #         if head in seen:
    #             return True
    #         seen.add(head)
    #         head = head.next

    #     return False
    f, s = head, head

    while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            return True

    return False

# O(N)
