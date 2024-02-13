# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4660/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

input = ListNode(1, 
                ListNode(2, 
                         ListNode(3, 
                                  ListNode(4,
                                           ListNode(5, ListNode(6))))))


def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

print(middleNode(input).val)