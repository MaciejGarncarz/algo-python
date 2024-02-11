#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4592/

from typing import List

input = ["h","e","l","l","o"]

def reverseString(s: List[str]) -> List[str]:
    left = 0
    right = len(s) - 1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
    
    return s

print(reverseString(input))
