from typing import List


input_nums = [1,1,1,0,0,0,1,1,1,1,0]
input_k = 2


def maxConsecutiveSubstring(nums: List[int], k:int) -> int:
    left = curr = ans = 0 
    for right in range(len(nums)):
        if nums[right] == 0:
            curr += 1
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        
        # if right == 9:
        #     a = 1213
        # print(list(range(left, right)))
        ans = max(ans, right - left + 1)

    return ans


print(maxConsecutiveSubstring(input_nums, input_k)) 