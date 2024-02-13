# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

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

input = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))


def pairSum(head: ListNode) -> int:
    answer = 0

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first = head
    prev = None
    curr = slow
    
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    head.show()
    


    while prev:
        sum = first.val + prev.val
        answer = max(answer, sum)
        first, prev = first.next, prev.next


    return answer


print(pairSum(input))


