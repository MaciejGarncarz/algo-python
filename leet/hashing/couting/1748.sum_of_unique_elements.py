# https://leetcode.com/problems/sum-of-unique-elements/description/

from typing import List


input = [1,2,3,2]

def sum_of_unique_elements(nums: List[int]) -> List[int]:
    hashMap = {}
    answer = 0
    for index, x in enumerate(nums):
        if x in hashMap:
            hashMap[x] += 1
        else:
            hashMap[x] = 0
    
    for key, value in hashMap.items():
        if value == 0:
            answer += key
    
    return answer


print(sum_of_unique_elements(input))