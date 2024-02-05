# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4661/

from typing import List


input = [1,1,3,3,5,5,7,7]

def countElements(arr: List[int]) -> int:
    elements = set(arr)
    count = 0
    for element in arr:
        if element + 1 in elements:
            count += 1

    return count


print(countElements(input))