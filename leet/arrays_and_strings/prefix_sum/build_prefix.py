from typing import List

input = [1, 6, 3, 2, 7, 2]

def buildPrefix(nums: List[int]) -> List[int]:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    return prefix

# prefix[-1] means prefix[len(prefix) - 1]. It just means get me last element of an array

print(buildPrefix(input))



