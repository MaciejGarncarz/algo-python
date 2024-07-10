# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

from heapq import *
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    heap = []

    for num in nums:
        heappush(heap, -num)
    
    for x in range(k-1):
        heappop(heap)

    return -heappop(heap)

nums = [3,2,1,5,6,4]
k = 2

print(findKthLargest(nums, k))

