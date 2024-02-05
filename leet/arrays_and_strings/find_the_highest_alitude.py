# https://leetcode.com/problems/find-the-highest-altitude/

from typing import List

input = [-4,-3,-2,-1,4,3,2]

def largestAltitude(gain: List[int]) -> int:
    prefix = [0]
    answer = 0

    for index in range(len(gain)):
        nextSum = prefix[index] + gain[index]
        prefix.append(nextSum)
        answer = max(answer, nextSum)

    return answer


print(largestAltitude(input))