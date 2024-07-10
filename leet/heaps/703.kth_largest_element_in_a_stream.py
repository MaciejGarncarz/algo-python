# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/708/heaps/4642/

from heapq import *
from typing import List


class KthLargest:
    heap = []
    indexToReturn: int

    def __init__(self, k: int, nums: List[int]):
        self.indexToReturn = k

        for num in nums:
            heappush(self.heap, -num)
        

    def add(self, val: int) -> int:
        heappush(self.heap, -val)

        temp = []
        for _ in range(self.indexToReturn):
            temp.append(heappop(self.heap))

        lastElement = temp[-1]

        for x in temp:
            heappush(self.heap, x)

        return -lastElement


# obj = KthLargest(3, [4,5,8,2])

# print(obj.add(3))
# print(obj.add(5))
# print(obj.add(10))
# print(obj.add(9))
# print(obj.add(4))

obj = KthLargest(1, [])

print(obj.add(-3))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(0))
print(obj.add(4))

        