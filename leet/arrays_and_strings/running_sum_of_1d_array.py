# Prefix techinique way

from typing import List

input = [1,2,3,4]

def buildPrefix(nums: List[int]) -> List[int]:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    return prefix

print(buildPrefix(input))