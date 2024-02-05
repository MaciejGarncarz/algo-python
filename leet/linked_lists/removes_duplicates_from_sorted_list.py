# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4597/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def show(self):
        counter = 0
        ptr: ListNode = self
        while ptr:
            print(f"At index {counter} value of node is {ptr.val}")
            counter += 1
            ptr = ptr.next

input = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

def deleteDuplicates(head: ListNode) -> ListNode:
    if head is None:
        return head
    
    current: head = head


    while current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head



print(deleteDuplicates(input).show())