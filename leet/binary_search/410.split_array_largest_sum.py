# https://leetcode.com/problems/split-array-largest-sum/description/

from typing import List


def splitArray(nums: List[int], k: int) -> int:
    left = max(nums)
    right = sum(nums)

    while left <= right:
        mid = (left + right) // 2
        splitRequired = 0
        currSum = 0

        for x in nums:
            if currSum + x <= mid:
                currSum += x
            else:
                currSum = x
                splitRequired += 1
        
        splitRequired += 1
        
        if splitRequired <= k:
            right = mid - 1
            minimumlargestSplitSum = mid
        else:
            left = mid + 1
        

    return minimumlargestSplitSum


# nums = [2,3,1,2,4,3]
# k = 5

nums = [7,2,5,10,8]
k = 2

print(splitArray(nums, k))