# https://leetcode.com/problems/move-zeroes/description/

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroFoundAt = 0  # O(1) space
        
        # If the current element is not 0, then we need to
        # append it just in front of last non 0 element we found.
        for i in range(len(nums)):  # O(n) time
            if nums[i] != 0:  # O(1) time
                nums[lastNonZeroFoundAt] = nums[i]  # O(1) time
                lastNonZeroFoundAt += 1  # O(1) time
        
        # After we have finished processing new elements,
        # all the non-zero elements are already at beginning of array.
        # We just need to fill remaining array with 0's.
        for i in range(lastNonZeroFoundAt, len(nums)):  # O(n) time
            nums[i] = 0  # O(1) time



obj = Solution()

print(obj.moveZeroes([0,1,0,3,12]))
print('sda')
        
        