# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4598/
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


# input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
input = ListNode(3, ListNode(5))
l = 1
r = 2

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if head is None or head.next is None:
        return head

    oneBeforeLeft = None
    leftNode = head
    index = 1
    while index != left:
        if index + 1 == left:
            oneBeforeLeft = leftNode
        index += 1
        leftNode = leftNode.next

    prev = None
    curr = leftNode
    while index < right + 1:
        index += 1
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    lastFromPrev:ListNode = prev    
    while lastFromPrev.next:
        lastFromPrev = lastFromPrev.next

    # Chain back again reverted list
    if oneBeforeLeft:
        oneBeforeLeft.next = prev
    else:
        head = prev

    lastFromPrev.next = curr
    return head

finalNode = reverseBetween(input, l, r)
finalNode.show()

# Check the solution for sure it could be do better and cleaner