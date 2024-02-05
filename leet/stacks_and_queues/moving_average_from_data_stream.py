# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/706/stacks-and-queues/4703/



from collections import deque


initial = 3
input =  [1, 10, 3, 5]

class MovingAverage:
    queue: deque
    def __init__(self, size: int):
        self.queue = deque(maxlen=size)
        

    def next(self, val: int) -> float:
        if len(self.queue) == self.queue.maxlen:
            self.queue.popleft()
        self.queue.append(val)
        sum = 0
        for item in self.queue:
            sum += item

        return sum / len(self.queue)
    
movingAverage = MovingAverage(initial)
for item in input:
    print(movingAverage.next(item))
        