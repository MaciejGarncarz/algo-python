# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/description/


# Definition for singly-linked list.
from math import ceil
from typing import Optional


class ListNode:
    def __init__(self, val:int=0, next = None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    map = []
    counter = 0
    while head is not None:
        map.append(head)
        counter += 1
        head = head.next
    
    mediumNode = counter // 2
    if mediumNode % 2 == 0:
        mediumNode + 1
        
    return map[mediumNode]

def middleNodePointers(head: Optional[ListNode]) -> Optional[ListNode]:
    middle = head
    last = head
    while last is not None and last.next is not None:
        middle = middle.next
        last = last.next.next

    return middle

node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = middleNode(node)
resultPointers = middleNodePointers(node)