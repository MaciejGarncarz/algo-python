# https://leetcode.com/problems/remove-linked-list-elements/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

input = ListNode(1, 
                 ListNode(2, 
                          ListNode(6, 
                                   ListNode(3, 
                                            ListNode(4, 
                                                     ListNode(5, 
                                                              ListNode(6)))))))
inputVal = 6

input = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
inputVal = 2


def remove_elements(head: ListNode, val: int):
    temp = ListNode(0)
    temp.next = head
    prev, curr = temp, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return temp.next


result = remove_elements(input, inputVal)
print()




