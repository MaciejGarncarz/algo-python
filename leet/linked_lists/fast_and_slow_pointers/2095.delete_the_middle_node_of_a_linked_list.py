# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


input = ListNode(1, # 1 - 3 - 4 - 7 - 1 - 2 - 6
                 ListNode(3, 
                          ListNode(4, 
                                   ListNode(7, 
                                            ListNode(1, 
                                                     ListNode(2, 
                                                              ListNode(6)))))))

input = ListNode(1)



def delete_middle(head: ListNode) -> ListNode:
    if(head.next == None):
        return None

    slow = head
    fast = head
    previous = head

    while fast and fast.next:
        previous = slow
        slow = slow.next
        fast = fast.next.next

    nodeToSwitch = slow.next
    slow.next = None
    previous.next = nodeToSwitch

    return head

def print_nodes(head: ListNode):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

result = delete_middle(input)
print_nodes(result)