
# 1480. Running sum of 1d array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

nums1 = [1, 2, 3, 4]
nums2 = [1, 1, 1, 1, 1]

def runningSum(nums: list[int]) -> list[int]:
    sums=0
    result=[]
    for i in nums:
        sums+=i
        result.append(sums)
    return result
    

print(runningSum(nums2))