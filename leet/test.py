# Two sorted array merged into one sorted array

from typing import List


input_1 = [1, 4, 7, 20]
input_2 = [3, 5, 6]

def merge_sorted(nums_1: List[int], nums_2: List[int]) -> List[int]:
    left = right = 0

    result = []

    while(left < len(nums_1)  and  right < len(nums_2)):
        leftValue = nums_1[left]
        rightValue = nums_2[right]


        if leftValue < rightValue:
            result.append(leftValue)
            left += 1
        else:
            result.append(rightValue)
            right += 1

    while left < len(nums_1):
        result.append(nums_1[left])
        left += 1
    
    while right < len(nums_2):
        result.append(nums_2[right])
        right += 1

    return result


print(merge_sorted(input_1, input_2))


