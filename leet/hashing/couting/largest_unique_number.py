# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4662/

from typing import List

input = [9,9,8,8]


def largestUniqueNumber(nums: List[int]) -> int:
    number_to_count = dict()

    for x in nums:
        value = number_to_count.get(x, 0)
        number_to_count[x] = value + 1

    answer = -1
    for key in number_to_count:
        count = number_to_count[key]
        if count == 1:
            answer = max(answer, key)

    return answer

print(largestUniqueNumber(input))