# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

from math import ceil
from typing import List
from heapq import *


def smallestDivisor(nums: List[int], threshold: int) -> int:
    heap = []
    def check(divisor: int):
        total = 0
        for num in nums:
            divisionResult = ceil(num / divisor)
            total += divisionResult
        
        return total <= threshold


    left = 1
    right = max(nums)

    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            heappush(heap, mid)
            right = mid - 1
        else: 
            left = mid + 1
    
    return heap[0]

nums1 = [91,41,78,86,8]
threshold1 = 114

nums2 = [44,22,33,11,1]
threshold2 = 5

print(smallestDivisor(nums2, threshold2))