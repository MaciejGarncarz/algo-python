# https://leetcode.com/problems/palindrome-linked-list/description/

from typing import Optional
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


input = ListNode(1, 
                 ListNode(2, 
                          ListNode(2, 
                                   ListNode(1))))

input2 = ListNode(1, ListNode(2))


def is_palindrome(head: Optional[ListNode]) -> bool:
    original = copy.deepcopy(head)
    current = head
    prev = None
    while current:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode

    while original:
        if original.val != prev.val:
            return False
        original = original.next
        prev = prev.next

    return True
        



result = is_palindrome(input)
print(result)