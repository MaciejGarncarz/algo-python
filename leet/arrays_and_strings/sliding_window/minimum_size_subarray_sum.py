# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List

input = [2,3,1,2,4,3]
t_input = 7

def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = sum = 0
    answer = len(nums)
    didItMatchTargetAtLeastOnce = False

    for i in range(len(nums)):
        sum += nums[i]
        while sum >= target:
            didItMatchTargetAtLeastOnce = True
            answer = min(answer, i - left + 1)
            sum -= nums[left]
            left += 1

    if didItMatchTargetAtLeastOnce == False:
        return 0
    
    return answer

print(minSubArrayLen(t_input, input))

