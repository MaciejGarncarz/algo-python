# https://leetcode.com/problems/find-pivot-index/description/


from typing import List


input = [2,1,-1]
# 1, 8, 11, 17, 22, 28

def find_pivot_index(nums: List[int]) -> int:
    prefix = [nums[0]]

    for x in range(1, len(nums)):
        prefix.append(nums[x] + prefix[-1])

    for x in range(0, len(prefix)):
        if x == 0:
            if prefix[x] == prefix[-1]:
                return 0
        else:
            if prefix[x] + prefix[x - 1] == prefix[-1]:
                return x
    
    return -1
            

print(find_pivot_index(input))


    
