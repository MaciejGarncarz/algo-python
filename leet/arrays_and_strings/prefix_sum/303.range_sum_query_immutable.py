# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List


class NumArray:
    originalNums = []
    prefix = []
    def __init__(self, nums: List[int]):
        self.originalNums = nums
        self.prefix.append(nums[0])
        
        for i in range(1, len(nums)):
            self.prefix.append(nums[i] + self.prefix[-1])
        

    def sumRange(self, left: int, right: int) -> int:
        if left <= 0:
            return self.prefix[right]
        else:
            return self.prefix[right] - self.prefix[left-1]
        

obj = NumArray([-1])
print(obj.sumRange(0, 0))