# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4594/

from typing import List

# 1.
# inputNums = [1,12,-5,-6,50,3]
# inputK = 4
# 2.
inputNums = [5]
inputK = 1


def findMaxAverage(nums: List[int], k: int) -> float:
    # Get current
    # Remove left index and add right index then get average
    current = 0
    rightIndex = k
    for i in range(k):
        current += nums[i]

    current = current / k 
    maxAverage = current

    for i in range(k, len(nums)):
        right = nums[rightIndex]
        left = nums[i - k]
        current = (current * k + right - left) / k
        maxAverage = max(maxAverage, current)
        rightIndex += 1

    return maxAverage

print(findMaxAverage(inputNums, inputK))

