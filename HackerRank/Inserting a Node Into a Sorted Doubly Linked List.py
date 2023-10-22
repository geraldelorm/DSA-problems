#!/bin/python3

import math
import os
import random
import re
import sys


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


def sortedInsert(head, data):
    # create the node
    node = DoublyLinkedListNode(data)

    #cas-1 list is empty
    if head == None:
        head = node

    #case-2 insert before head
    elif data < head.data:
        node.next = head
        head.prev = node
        head = node

    #case-3 insert at speacific position or at the end

    else:
        cur = head
    #transerve to specific element.
        while cur.next != None and cur.data < data:
            cur = cur.next

    #insert at the end
        if cur.next == None and cur.data < data:
           cur.next = node
           node.prev = cur
    #insert at specific position
        else:
            previous = cur.prev
        #change previous node
            previous.next = node
            node.prev = previous

        #change in current node
            node.next = cur
            cur.prev = node
    return head


# O(N)

if __name__ == '__main__':
