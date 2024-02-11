# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4602/

from typing import List


input_nums = [9,6,4,2,3,5,7,0,1]

def findMissingNumber(nums: List[int]) -> int:
    numbers = set(range(0, len(nums) + 1))
    for num in numbers:
         if num not in nums:
              return num

    return 0


print(findMissingNumber(input_nums))