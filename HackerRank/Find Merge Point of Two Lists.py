#!/bin/python3

import collections
import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#


def findMergeNode(head1, head2):
    l1_stack, l2_stack = collections.deque(), collections.deque()
    curr1, curr2 = head1, head2
    # l1, l2, diff = 0, 0, 0

    while curr1:
        l1_stack.append(curr1)
        # l1 += 1
        curr1 = curr1.next

    while curr2:
        l2_stack.append(curr2)
        # l2 += 1
        curr2 = curr2.next

    # diff = abs(l1 - l2);

    # curr1, curr2 = head1, head2
    # if l1 > l2:
    #     for i in range(diff):
    #         curr1= curr1.next
    # elif l1 > l2:
    #     for i in range(diff):
    #         curr2= curr2.next

    # while curr1 and curr2:
    #     if curr1 == curr2:
    #         return curr2.data
    #     curr1 = curr1.next
    #     curr2 = curr2.next

    intersection = None

    while l1_stack and l2_stack:
        s1, s2 = l1_stack.pop(), l2_stack.pop()
        if s1 == s2:
            intersection = s1.data

    return intersection


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head
        ptr2 = llist2.head

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next

        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()
