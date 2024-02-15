# https://leetcode.com/problems/implement-stack-using-queues/description/

import collections

class MyStack:
    queue1 = collections.deque()
    queue2 = collections.deque()
    useQueue1 = True
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue1 = collections.deque()
        self.useQueue1 = True
        return None

    def push(self, x: int) -> None:
        if self.useQueue1 == True:
            if len(self.queue2) == 0:
                self.queue1.append(x)
            else:
                while len(self.queue2) != 0:
                    self.queue1.append(self.queue2.popleft())
                self.queue1.append(x)
            self.useQueue1 = False
        else:
            while len(self.queue1) != 0:
                self.queue2.append(self.queue1.popleft())
            self.queue2.append(x)
            self.useQueue1 = True

    def pop(self) -> int:
        if self.useQueue1 == True:
            while len(self.queue2) != 1:
                self.queue1.append(self.queue2.popleft())
            self.useQueue1 = False
            return self.queue2.popleft()
        else:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.popleft())
            self.useQueue1 = True
            return self.queue1.popleft()
        

    def top(self) -> int:
        if self.useQueue1 == True:
            return self.queue2[-1]
        else:
            return self.queue1[-1]
        

    def empty(self) -> bool:
        return len(self.queue2) == 0 and len(self.queue1) == 0
    

result = MyStack()

# result.push(1)

# b = result.pop()
c = result.empty()

print('t')
