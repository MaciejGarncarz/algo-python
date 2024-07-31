# https://leetcode.com/problems/minimum-common-value/description/

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = right = 0

        while left < len(nums1) and right < len(nums2):
            leftValue = nums1[left]
            rightValue = nums2[right]

            if leftValue == rightValue:
                return leftValue
            
            if leftValue > rightValue:
                right += 1
            else:
                left += 1
        
        return -1
        