# https://leetcode.com/problems/k-radius-subarray-averages/description/

from math import floor
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix = [nums[0]]
        answer = []
        n = len(nums)
        left = 0
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])

        if k == 0:
            return nums
        
        for i in range(n):
            if i - k < 0 or i + k >= n:
                answer.append(-1)
            else:
                maxRadius = prefix[i + k]
                if i - k > 0:
                    diviser = k * 2 + 1
                    result = (maxRadius - prefix[left]) // diviser
                    answer.append(floor(result))
                    left += 1
                else:
                    diviser = k * 2 + 1
                    result = maxRadius // diviser
                    answer.append(result)
        
        return answer
    

obj = Solution()
print(obj.getAverages([40527,53696,10730,66491,62141,83909,78635,18560], 2))

